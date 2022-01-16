import cv2
import mediapipe as mp

def distance(pos1, pos2):
    x1, y1 = pos1[0], pos1[1]
    z1, z2 = pos1[2], pos2[2]
    x2, y2 = pos2[0], pos2[1]
    distance = ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5
    return distance

def collect_data_recording(mp_drawing,mp_drawing_styles,mp_hands,caption):
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        success, image = caption.read()
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        points = results.multi_hand_landmarks
    
        if points:
            for hand_landmarks in points:
                    mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
            LOP = [[data_point.x, data_point.y,
                               data_point.z] for data_point in points[0].landmark]
            
            mains = {"paume":LOP[0],
            "thumb1":LOP[1],"thumb2":LOP[2],"thumb3":LOP[3],"thumb4":LOP[4],
            "index1":LOP[5],"index2":LOP[6],"index3":LOP[7],"index4":LOP[8],
            "middle1":LOP[9],"middle2":LOP[10],"middle3":LOP[11],"middle4":LOP[12],
            "ring1":LOP[13],"ring2":LOP[14],"ring3":LOP[15],"ring4":LOP[16],
            "pinky1":LOP[17],"pinky2":LOP[18],"pinky3":LOP[19],"pinky4":LOP[20],}
        else:
            mains = None

    return [mains,image]


def pinch(finger1,finger2):
    if distance(finger1,finger2)<0.1:
        return True
    else:
        return False

def closed_hand(finger1,finger2,finger3,finger4,hand,level):
    if level == 'niveau 3':
        a = 0.3
        b = 0.2
    elif level == 'niveau 2':
        a = 0.5
        b = 0.4
    else:
        a = 0.7
        b = 0.6

    if distance(finger1,hand)<a and distance(finger2,hand)<b and distance(finger3,hand)<b and distance(finger4,hand)<a:
        return True
    else:
        return False

def test():
    cam = cv2.VideoCapture(0)
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    while True:
        data = collect_data_recording(mp_drawing,mp_drawing_styles,mp_hands,cam)
        if data:
            print(pinch(data["thumb4"],data["index4"]))

# test()
