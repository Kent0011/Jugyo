import sys
from PyQt5.QtWidgets import QApplication
from cas_gui.base import CAS_GUI
from cas_gui.threads.image_processor_class import ImageProcessorClass
from scipy.ndimage import gaussian_filter
import numpy as np

# 処理クラスの定義
class Filter(ImageProcessorClass):
    last_frame = None
    def process(self, inputFrame):
        if self.last_frame is None:
            self.last_frame = inputFrame
            return inputFrame
        else:
            diff = np.abs(inputFrame.astype(np.float32) - self.last_frame.astype(np.float32))
            diff = np.clip(diff, 0, 255).astype(np.uint8)
            self.last_frame = inputFrame
            return diff

# GUIクラスの定義
class ExampleGUI(CAS_GUI):
    def __init__(self):
        self.processor = Filter
        super().__init__()
        print("FILTER SET")

# 実行エントリポイント
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    
    try:
        window = ExampleGUI()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
