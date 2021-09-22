
import cv2
#使用函数cv2.imread()䖪入图像。䦈幅图像应䖔在此程序的工作䞞径虽或者给函数提供完整䞞径虽
img = cv2.imread('./imge/leimu.jpg')
#显示图像
cv2.imshow('leimu', img)

#cv2.waitKey()是一个仝盘绑定函数。需要指出的是它的时间尺度是毫秒级。函数等待特定的几毫秒虽看是否有仝盘䥂入。
# 特定的几毫秒之内虽如果按下任意键，这个函数会返回按键的ASCII码值虽程序将会继续运行。如果没有仝盘䥂入虽䦃回值为-1虽如果我们䕭置䦈个函数的参数为0虽䩒它将会无俿期的等待仝盘䥂入。
# 它也可以䉚用来检测特定仝是否䉚按下虽例如按仝a是否䉚按下虽䦈个后儑我们会接着䕗䕩。
cv2.waitKey(0)
# cv2.destroyAllWindows()可以䤪易删倓任何我们建立的窗口。如果你想删倓特定的窗口可以使用cv2.destroyWindow()虽在括号内䥂入你想删倓的窗口名。
cv2.destroyAllWindows()
#保存图像
cv2.imwrite('./imge/leimu1.jpg', img)

