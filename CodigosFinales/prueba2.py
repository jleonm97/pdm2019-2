import puerta_clasificatoria as pc
import cv2

cap = cv2.VideoCapture(0)
mnh = 35
mxh = 75
mns = 50
mxs = 250
mnv = 35
mxv = 250
mnh2 = 100
mxh2 = 125
mns2 = 65
mxs2 = 250
mnv2 = 75
mxv2 = 250
while True:
    try:
        (Xc,Yc,Area,im) = pc.coorBoundingBoxes2(cap,2,mnh,mxh,mns,mxs,mnv,mxv,mnh2,mxh2,mns2,mxs2,mnv2,mxv2)

    except:
        print('falla')
        (Xc, Yc, Area, im) = pc.falla(cap)
    cv2.imshow("Hola", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()