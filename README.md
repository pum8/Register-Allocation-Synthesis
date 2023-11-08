# Register-Allocation-Synthesis

The Compiler Graph Generator (CGG) is a tool designed for creating Static Single Assignment (SSA) graphs. It offers two execution methods: one via the command line interface (CMD) and the other as an object. To run CGG via CMD, follow these instructions:

## Installation

Clone this repository to your local machine.

   ```bash
   git clone https://git.txstate.edu/your-username/Register-Allocation-Synthesis.git
   cd Register-Allocation-Synthesis
   ```
   
## Usage
To generate a SSA graph with Live Ranges, run the CGG_CMD.py script with two parameters:

CGG.py [Number of nodes for the SSA graph] [Live range density]

Here's an example command:

   ```bash
   python CGG_CMD.py 10 50
   ```
In this example, 10 is the number of nodes for the SSA graph, and 50 is the Live range density.

To implement it within a code block:
```python
from CGG import Generator

GG = Generator()
GG.graphCreation(10,50)
```
To implement **ProgramGenerator** within a code block:
```python
from ProgramGenerator import ProgramGeneratorOBJ

program_generator = ProgramGeneratorOBJ()
split_programs = program_generator.randomSplitGenerator(10,10)
```
**Interpreter**:

```python
from interpreter import interpreter
from CGG import Generator
from ProgramGenerator import ProgramGeneratorOBJ

GG = Generator()
GG.graphCreation(10,50)
program_generator = ProgramGeneratorOBJ()
split_programs = program_generator.randomSplitGenerator(10,10)
SSA,LV = interpreter().execute(GG,split_programs)
```
