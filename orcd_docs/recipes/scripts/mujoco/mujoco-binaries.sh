-8<-- [start:login]
wget https://github.com/deepmind/mujoco/releases/download/2.3.0/mujoco-2.3.0-linux-x86_64.tar.gz
tar -xzf mujoco-2.3.0-linux-x86_64.tar.gz
-8<-- [end:login]

-8<-- [start:path]
export MUJOCO_PY_MUJOCO_PATH=$HOME/path/to/mujoco230/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MUJOCO_PY_MUJOCO_PATH/bin
-8<-- [end:path]

-8<-- [start:env-var]
echo MUJOCO_PY_MUJOCO_PATH
echo LD_LIBRARY_PATH
-8<-- [end:env-var]