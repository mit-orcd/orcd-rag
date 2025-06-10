-8<-- [start:venv]
module load anaconda/2023a
mkdir /state/partition1/user/$USER
python -m venv /state/partition1/user/$USER/mujoco_env
source /state/partition1/user/$USER/mujoco_env/bin/activate
pip install 'mujoco-py<2.2,>=2.1'
-8<-- [end:venv]

-8<-- [start:pkgs]
pip install pkgname1
pip install pkgname2
-8<-- [end:pkgs]

-8<-- [start:python]
python
import mujoco_py
-8<-- [end:python]

-8<-- [start:directory]
cp -r /state/partition1/user/$USER/mujoco_env $/software/mujoco/
-8<-- [end:directory]

