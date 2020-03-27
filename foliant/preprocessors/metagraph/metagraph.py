'''
Preprocessor for Foliant documentation authoring tool.
Generates graphviz diagram based on metadata.
'''

from foliant.preprocessors.utils.preprocessor_ext import (BasePreprocessorExt,
                                                          allow_fail)
from foliant.meta.generate import load_meta
from .draw import ChaptersGraph


class Preprocessor(BasePreprocessorExt):
    tags = ('metagraph',)
    defaults = {
        'natural': False,
        'directed': False,
        'draw_all': False,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.logger = self.logger.getChild('metagraph')

        self.logger.debug(f'Preprocessor inited: {self.__dict__}')

    @allow_fail()
    def process_metagraph_blocks(self, block) -> str:

        self.logger.debug(f'Processing metagraph tag in {self.current_filepath}')
        meta = load_meta(self.config.get('chapters', []))
        graph = ChaptersGraph(meta, self.options)
        return graph.draw()

    def apply(self):
        self._process_tags_for_all_files(func=self.process_metagraph_blocks)
        self.logger.info('Preprocessor applied')
