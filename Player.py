import numpy as np
import cv2


class PlayerPoint:
    def __init__(self):
        self.gx = []
        self.gy = []

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.gx.append(x)
            self.gy.append(y)

    def get_last_x(self):
        return self.gx[-1]

    def get_last_y(self):
        return self.gy[-1]

    def get_coords(self):
        img = np.zeros((512,512,3), np.uint8) # new black image

        while(1):
            cv2.imshow('image', img)
            cv2.setMouseCallback('image', self.click_event)
            k = cv2.waitKey(20) & 0xFF
            if k == ord('p'): # p - print on the screen
                font = cv2.FONT_HERSHEY_SIMPLEX
                str_coords_x_y = str(self.get_last_x()) + ', ' +str(512-self.get_last_y())
                cv2.putText(img, str_coords_x_y, (self.get_last_x(), self.get_last_y()), font, 1, (255,0,0),2)

            elif k == ord('s'): # s - save last point and exit
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return self.get_last_x(), 512-self.get_last_y()

            elif k == ord('c'): # c - clear the image (hide the text)
                img = np.zeros((512,512,3), np.uint8) # hide text (reset image to black)

            elif k == 27:
                break
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("You didn't save your point! :(")
        return -1, -1
