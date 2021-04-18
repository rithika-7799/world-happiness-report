This is a project that uses C# as front end and Python as DLL.
Data analysis is done using python3 on the world happinedd report. The graphs and plots obtained are saved onto the system.
C# uses windows forms as UI. 
It displayed these saved images.

Python script is compiled into a DLL as follows:
C# class library type project is opened and the python script is run by spawning another process.
This is built and .ddl file is created.
The DLL is imported into frontend form with "using" statement, and adding the reference. 
