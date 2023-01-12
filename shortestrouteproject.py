import PySimpleGUI as sg
import heapq

def dijkstra(graph, start, goal):

    queue = []
    heapq.heappush(queue, (0, start))
    visited = set()
    previous = {start: None}
    distances = {start: 0}

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return (distances[goal], build_path(previous, goal))
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return float("inf")


def build_path(previous, goal):
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = previous[node]
    return path[::-1]

def calculations(destination):

    graph = {
        "A": {"B": 3},
        "B": {"A": 3, "C": 6, "D": 3},
        "C": {"B": 6, "E": 9},
        "D": {"B": 3, "F": 2 , "K": 7},
        "E": {"C": 9, "G": 4},
        "F": {"D": 2, "G": 7,"H": 13, "I": 6, "J": 7},
        "G": {"E": 4, "F": 7, "H": 5},
        "H": {"F": 13, "G": 5, "I": 10},
        "I": {"F": 6, "H": 10},
        "J": {"F": 7, "K": 8},
        "K": {"D": 7, "J": 8}
    }

    str1 = dijkstra(graph, "A", destination)
    str2 = dijkstra(graph, "H", destination)
    str3 = dijkstra(graph, "K", destination)

    locationDictionary = {
        "A": "Hospital Serdang",
        "B": "B11",
        "C": "903",
        "D": "Persiaran Jaya",
        "E": "B50",
        "F": "E18",
        "G": "E7",
        "H": "Hospital Kajang",
        "I": "Semenyih",
        "J": "Seksyen 8",
        "K": "Hospital Az-Zahra"
    }

    distanceSerdang = str1[0]
    distanceKajang = str2[0]
    distanceZahra = str3[0]


    str4 = str1[1]
    str5 = str2[1]
    str6 = str3[1]

    resultA = str(locationDictionary[str4[0]])
    resultB = str(locationDictionary[str5[0]])
    resultC = str(locationDictionary[str6[0]])

    for i in range(1, len(str4)):

        resultA = resultA + " → " + str(locationDictionary[str4[i]])

    for i in range(1, len(str5)):

        resultB = resultB + " → " + str(locationDictionary[str5[i]])

    for i in range(1, len(str6)):

        resultC = resultC + " → " + str(locationDictionary[str6[i]])

    print(resultA)
    print(resultB)
    print(resultC)
    results = [resultA, resultB, resultC]

    return '\n'.join(str(x) for x in results)

sg.theme('default1')  # Add a touch of color

# All the stuff inside your window.
layout1 = [

    [
        sg.Radio('B11', "RADIO1", default=False),
        sg.Radio('903', "RADIO1"),
        sg.Radio('Persiaran Jaya', "RADIO1"),
        sg.Radio('B50', "RADIO1"),
        sg.Radio('E18', "RADIO1"),
        sg.Radio('E7', "RADIO1"),
        sg.Radio('Semenyih', "RADIO1"),
        sg.Radio('Seksyen 8', "RADIO1")
    ],

    [
        sg.OK(), sg.Button('Cancel')
    ],

    [
        sg.Text("FASTEST ROUTE\n", visible=False, key='fastest'),
        sg.Text(calculations("C"), visible=False, key='results')
    ]

]

# Create the Window
window = sg.Window('Shortest Route Project', layout1)

# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == "OK":
        print(event)
        window['fastest'].update(visible=True)

        if values[0] == True:

            window['results'].update(calculations("B"), visible=True)

        if values[1] == True:

            window['results'].update(calculations("C"), visible=True)

        if values[2] == True:

            window['results'].update(calculations("D"), visible=True)

        if values[3] == True:

            window['results'].update(calculations("E"), visible=True)

        if values[4] == True:

            window['results'].update(calculations("F"), visible=True)

        if values[5] == True:

            window['results'].update(calculations("G"), visible=True)

        if values[6] == True:

            window['results'].update(calculations("I"), visible=True)

        if values[7] == True:

            window['results'].update(calculations("J"), visible=True)

window.close()

