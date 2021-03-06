#encoding: UTF-8
'''This file contains all the functions that liase the database with the UI'''
#Make sure you're using Python3
#All code is by David, unless otherwise stated

from dbHandler import *


crDB = DbConn("db/crDBv2.db")
c = crDB.cursor

#Functions
def getModules(teacherID):
    c.execute('SELECT * FROM groupset WHERE teacherID = ?', [teacherID])
    modules = c.fetchall()
    i = 0 
    for x in modules:
        modules[i] = x[4] + " Set " + x[1]
        i += 1
    return modules

def getModuleInfo(module): #Get module deets
    c.execute('SELECT * FROM module WHERE moduleCode = ?', [module])
    line = c.fetchall()
    deets = line[0] #Select the frist and only tuple in the list
    moduleInfo = deets[1], deets[2], "\n" + deets[3]
    #print(moduleInfo) #print selected data with spacing
    return moduleInfo

def displayGrades(selectedModule):
    module = selectedModule[:6]
    setName = selectedModule[-1:]
    title = "Getting grades for", selectedModule, "..."
    #print(title)
    header = '%15s' % "Student ID",  '%15s' % "Name", '%13s' % "Surname",  '%6s' % "Grade"
    #print(header)
    c.execute('SELECT groupsetID FROM groupset WHERE moduleCode = ? AND groupsetName = ?', [module, setName])
    setID = c.fetchall()[0][0]
    print(setID)
    c.execute('SELECT * FROM grade WHERE groupsetID = ?', [setID]) #Get grades
    allGrades = c.fetchall()
    moduleList = []
    for grade in allGrades: #go through all the rows
        studentId = grade[3] #Find the student ID
        c.execute('SELECT * FROM student WHERE studentID = ?', [studentId])
        line = c.fetchall() #Get student deets
        user = line[0] #Select the frist and only tuple in the list         
        moduleItem = '%15s' % user[1], '%15s' % user[3], '%13s' % user[4], '%6s' % grade[0]
                     #selected data with spacing
        #print(moduleItem)
        moduleList.append(moduleItem)
    return (title, header, moduleList)
        
def displayModules(teacher):
    c.execute('SELECT * FROM teacher WHERE teacherID = ?', [teacher])
    #Get teacher info
    line = c.fetchall() #[0]?
    user = line[0] #Select the first and only tuple in the list
    title = "Getting your modules, ", user[2],  user[3], user[4], "..."
    header = '%15s' % "Module Code",  '%15s' % "Module Name", '%13s' % "Module Desc."
    c.execute('SELECT moduleCode FROM teachedby WHERE teacherID = ?', [teacher])
    modules = c.fetchall() #Get modules
    i = 0 
    for x in modules:
        modules[i] = x[0]
        i += 1
    moduleList = []
    for module in modules:
        c.execute('SELECT * FROM module WHERE moduleCode = ?', [module])
        #Get modules
        line = c.fetchall()
        mod = line[0][1:]
        moduleList.append(mod)
    #print(moduleList)
    '''Example: [('M01001', 'Art of nothing', 'Nobody helped me out,
    so no description, you write better if you want'), ...]'''
    
    return title, header, moduleList

def diplayMyGrades(student): #TODO David
    return 0
    
#TODO-David Teacher navigation between modules summary, single module, attendance, 

#TESTING:
#getModuleInfo("M03010")
displayGrades('M03010 Set a')
#displayModules("st144228203")
#print(getModules('st82277'))
#diplayMyGrades(student)
'''
Deprecated code: Leave for reference. Thanks. David.
##############
First attempt
    def displayGrades(module):
    #now displays whose PW is p@assword, working on how to fetch from different tables
        #print contents of all columns for row that match a certain value in a column

        #c.execute('SELECT * FROM student WHERE studentPassword = "p@ssword"')
        c.execute('SELECT * FROM student WHERE studentPassword = ?', [module]) #Thanks Gary for the fix

        all_rows = c.fetchall()
        for user in all_rows: #go through all the rows
            print(user[1], '%10s' % user[3], '%13s' % user[4], user[5],) #print selected data with spacing

#################
Old BD connection
    import sqlite3
    connect to the DB (run dbHandler.py first)
    conn = sqlite3.connect('db/crDB.db')
    c = conn.cursor()
    
#################################
Alternative way to remove tuples
    i = 0
    while (i < len(modules)):
        modules[i] = modules[i][0]
        i+=1

'''
