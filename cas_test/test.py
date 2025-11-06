import sys
from PyQt5.QtWidgets import QApplication
from cas_gui.base import CAS_GUI
from cas_gui.threads.image_processor_class import ImageProcessorClass
from scipy.ndimage import gaussian_filter
import numpy as np

# 処理クラスの定義
class Filter(ImageProcessorClass):
    def process(self, inputFrame):
        # パワースペクトル（パワースペクトル密度）の計算
        # 入力：inputFrame（2D numpy配列、画像）
        # 出力：パワースペクトル画像（logスケールで正規化表示）

        # 2次元FFT
        f = np.fft.fft2(inputFrame)
        fshift = np.fft.fftshift(f)

        # パワースペクトル
        psd2D = np.abs(fshift) ** 2

        # logスケールに変換（可視化のため、+1でlog(0)回避）
        psd2D_log = np.log(psd2D + 1)

        # 0-255に正規化して画像として返す
        psd2D_norm = 255 * (psd2D_log - psd2D_log.min()) / (psd2D_log.max() - psd2D_log.min())
        return psd2D_norm.astype(np.uint8)

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
