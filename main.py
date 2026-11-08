import mujoco
import mujoco.viewer
from pathlib import Path

SKRYPT_DIR = Path(__file__).resolve().parent
modelPath = SKRYPT_DIR / "model" / "ramie.xml"
model = mujoco.MjModel.from_xml_path(str(modelPath))

data = mujoco.MjData(model)

with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
        mujoco.mj_step(model, data)
        viewer.sync()
