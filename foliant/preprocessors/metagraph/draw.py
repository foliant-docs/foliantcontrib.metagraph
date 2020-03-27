from pygraphviz import AGraph

from foliant.meta.classes import Meta

REL_KEY = 'relates'
GV_KEY = 'gv_attributes'


class ChaptersGraph:
    """Class which builds, holds and draws a chapters graph"""

    def __init__(self, chapters_meta: Meta, config: dict = {}):
        self.meta = chapters_meta
        self.config = config
        self.node_names = []

    def draw(self):
        """Draw graph with graphviz and save it to self.config['filename']"""

        default_gv_attributes = {
            'node': {'shape': 'rect', 'fontname': 'PT Sans'},
            'edge': {'arrowhead': 'open', 'arrowtail': 'open', 'fontname': 'PT Sans'},
            'graph': {'fontname': 'PT Sans'}
        }

        directed = self.config.get('directed', False)
        attrs = self.config.get('gv_attributes', default_gv_attributes)
        g = AGraph(directed=directed, strict=False)
        for k, v in attrs.get('graph', {}).items():
            g.graph_attr[k] = v
        for k, v in attrs.get('node', {}).items():
            g.node_attr[k] = v
        for k, v in attrs.get('edge', {}).items():
            g.edge_attr[k] = v
        self._draw_nodes(g)
        self._draw_edges(g, self.config.get('natural', False))
        return g.string()

    def _draw_nodes(self, graph: AGraph):
        for section in self.meta.iter_sections():
            if self.config['draw_all'] or section.data.get('draw', False):
                title = section.data.get('title', section.title)
                graph.add_node(section.id,
                               label=title)

    def _draw_edges(self, graph: AGraph, natural: bool):
        def add_child_edges(section):
            for child in section.children:
                graph.add_edge(section.id, child.id)
                add_child_edges(child)
        if natural:
            for chapter in self.meta.chapters:
                add_child_edges(chapter.main_section)
        else:
            for section in self.meta.iter_sections():
                if self.config['draw_all'] or section.data.get('draw', False):
                    if REL_KEY in section.data:
                        id_list = section.data[REL_KEY]
                        if not isinstance(id_list, list):
                            id_list = [id_list]
                        for rel_id in id_list:
                            graph.add_edge(section.id, rel_id)
