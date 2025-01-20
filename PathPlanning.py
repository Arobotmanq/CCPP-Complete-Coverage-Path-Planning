#!bin/bash/python3
# wadl
from mywadl.survey import Survey
from mywadl.mission import Mission
# paramters
from mywadl.solver.solver import SolverParameters
from mywadl.lib.route import RouteParameters
from mywadl.mission import MissionParameters
for i in range(1):
    #read keypoints in txt file
    fr = open("PathplanningIn.txt",'r')
    linelist=[]
    for line in fr.readlines():
        line=line.replace("\n","")
        linevalue=float(line)
        linelist.append(linevalue)
    fr.close()
    A_long=linelist[0]
    A_lat=linelist[1]
    B_long=linelist[2]
    B_lat=linelist[3]
    C_long=linelist[4]
    C_lat=linelist[5]
    D_long=linelist[6]
    D_lat=linelist[7]
    
    # A_long=91.83756256103516
    # A_lat=35.47226497
    # B_long=91.82593536376953
    # B_lat=35.47226497
    # C_long=91.83485412597656
    # C_lat=35.47226497
    # D_long=91.85092163085938
    # D_lat=35.47226497
    
    # E_lat=linelist[8]
    # E_long=linelist[9]
    # F_lat=linelist[10]
    # F_long=linelist[11]
    # suvey design script
    # get file name
    # files are assumed geofences (ID, lat, long)
    file = "ZhuonaiLake.csv"
    
    # make survey
    name = 'ZhuonaiLake'
    survey = Survey(name)
    
    # add the keypoints
    keyPoints = {"A": (A_lat, A_long),
                  "B":  (B_lat, B_long),
                "C":  (C_lat, C_long),
                  "D":  (D_lat, D_long),
                # "E":  (E_lat, E_long),
                # "F":  (F_lat, F_long)
                 }
    survey.setKeyPoints(keyPoints)
    
    # route paramters
    routeParams = RouteParameters()
    routeParams["limit"] = 28*60,  # s
    routeParams["speed"] = 5  # m/s
    routeParams["altitude"] = 50.0  # m
    # add the tasks
    
    survey.addTask(file,
                   step=100,
                   home=["A","B","C","D"],
                   routeParameters=routeParams,
                   )
    
    # solver parameters
    solverParams = SolverParameters()
    solverParams["subGraph_size"] = 10
    solverParams["SATBound_offset"] = 4
    solverParams["timeout"] = 60
    
    # set the solver parameters
    survey.setSolverParamters(solverParams)
    
    # plan the survey
    view = 0
    # view current plan
    if view == 1:
        survey.view()
    else:
        # run path solver to plan paths and write output
        #print(1)
        survey.plan()
        #survey.plot()
    
    # make mission
    # mission paramters
    missionParams = MissionParameters()
    missionParams["N_bands"] = 4
    missionParams["autoland"] = False
    
    missionParams["assign"] = "sequence"
    
    missionParams["offset_takeoff_dist"] = 10
    missionParams["offset_land_dist"] = 10
    
    
    mission = Mission(missionParams)
    mission.fromSurvey(survey, showPlot=True)
    mission.setVersion(4, 0, 187)
    mission.write()
