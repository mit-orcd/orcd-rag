-8<-- [start:module]
module load anaconda3/2022.10
-8<-- [end:module]

-8<-- [start:install]
pip install --user 'mujoco-py<2.2,>=2.1'
-8<-- [end:install]

-8<-- [start:python]
python
import mujoco_py
-8<-- [end:python]

