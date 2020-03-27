[![](https://img.shields.io/pypi/v/foliantcontrib.metagraph.svg)](https://pypi.org/project/foliantcontrib.metagraph/)  [![](https://img.shields.io/github/v/tag/foliant-docs/foliantcontrib.metagraph.svg?label=GitHub)](https://github.com/foliant-docs/foliantcontrib.metagraph)

# MetaGraph preprocessor for Foliant

Preprocessor generates Graphviz diagrams of meta sections in the project.

## Installation

```bash
$ pip install foliantcontrib.metagraph
```

## Config

```yaml
preprocessors:
    - metagraph:
        natural: false
        directed: false
        draw_all: false
```

`natural`
:   if `true` — the graph is generated based on "natural" section structure: main sections are connected to the inner sections, which are connected to their child sections and so on. If `false` — the connections are deretmined by the `relates` meta section of each chapter. Default: `false`

`directed`
:   If `true` — draws a directed graph (with arrows). Default: `false`

`draw_all`
:   If `true` — draws all sections, except those which have meta field `draw: false`. If `false` — draws only sections which have meta field `draw: true`. Default: `false`

## Usage

First set up a few meta sections:

```html
<meta title="Main document" id="main" relates="['first', 'sub']" draw="true"></meta>

# First title
<meta id="first" draw="true"></meta>

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nesciunt, atque.

## Subtitle

<meta id="sub"  draw="true"></meta>
```

Then add a `metagraph` tag somewhere in the project:

```html
<metagraph></metagraph>
```
