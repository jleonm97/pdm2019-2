
import puerta_clasificatoria as pc
import cv2

cap = cv2.VideoCapture(0)
mnh = 35
mxh = 75
mns = 50
mxs = 250
mnv = 35
mxv = 250
while True:
    try:
        (Xc,Yc,Area,im) = pc.coorBoundingBoxes(cap,1,mnh,mxh,mns,mxs,mnv,mxv)

    except:
        print('falla')
        (Xc, Yc, Area, im) = pc.falla(cap)
    cv2.imshow("Hola", im)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()