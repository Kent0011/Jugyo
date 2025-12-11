import sys
from PyQt5.QtWidgets import QApplication
from cas_gui.base import CAS_GUI
from cas_gui.threads.image_processor_class import ImageProcessorClass
import numpy as np

# 処理クラスの定義
class Filter(ImageProcessorClass):
    last_frame = None
    def process(self, inputFrame):
        a = inputFrame.astype(np.float32)
        if self.last_frame is None:
            self.last_frame = a
        b = np.rot90(np.rot90(self.last_frame))
        
        self.last_frame = a

        a_fft = np.fft.fftshift(np.fft.fft2(a))
        b_fft = np.fft.fftshift(np.fft.fft2(b))
        conv = np.fft.ifft2(a_fft*b_fft)
        return np.abs(np.fft.fftshift(conv))

# GUIクラスの定義
class ExampleGUI(CAS_GUI):
    def __init__(self):
        self.processor = Filter
        super().__init__()

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
