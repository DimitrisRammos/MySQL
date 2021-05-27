# ----- CONFIGURE YOUR EDITOR TO USE 4 SPACES PER TAB ----- #
import settings
import sys,os
sys.path.append(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'lib'))
import pymysql #as db

def connection():
    ''' User this function to create your connections '''
    # con = db.connect(
    #     settings.mysql_host, 
    #     settings.mysql_user, 
    #     settings.mysql_passwd, 
    #     settings.mysql_schema)

    con = pymysql.connect(host='localhost', user='root', password='', db = 'sys') 
    return con

def mostcommonsymptoms(vax_name):
    
    # Create a new connection
    # Create a new connection
    con=connection()
    # Create a cursor on the connection
    cur=con.cursor()
    
    return [("vax_name","result")]


def buildnewblock(blockfloor):
    
   # Create a new connection
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    
 
    return [("result",),]

def findnurse(x,y):

    # Create a new connection
    
    con=connection()
    
    # Create a cursor on the connection
    cur=con.cursor()
    cur.execute(f"SELECT N.Name, N.EmployeeID, (SELECT count( distinct v.patient_SSN) AS num FROM vaccination v WHERE( v.nurse_EmployeeID = N.EmployeeID)) AS NUM_PATIENT_VACCINATION FROM nurse N WHERE( N.EmployeeID IN ( SELECT oc.Nurse FROM on_call oc WHERE (oc.BlockFloor = {x}) GROUP BY oc.Nurse HAVING ( count( distinct oc.BlockCode) = (	SELECT count(*) FROM block bl WHERE (bl.BlockFloor = {x}) ) ) ) AND {y} <= ( SELECT count(distinct ap.Patient) FROM appointment ap WHERE (ap.PrepNurse = N.EmployeeID) ) ) GROUP BY N.Name, N.EmployeeID")

    #print because with have ERROR 500
    print(("Nurse", "ID", "Number of patients"))
    rows = cur.fetchall()
    for row in rows:
    	print(row)

    #return
    return [("Nurse", "ID", "Number of patients"), cur.fetchall()]

def patientreport(patientName):
    # Create a new connection
    con=connection()

    # Create a cursor on the connection
    cur=con.cursor()

    return [("Patient","Physician", "Nurse", "Date of release", "Treatement going on", "Cost", "Room", "Floor", "Block"),]

findnurse(1,2)
