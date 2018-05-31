# Online-Judiciary-System[Django web application]

In our software(Online judiciary system) the user will be required to log in to the system, after which 
depending on his role i.e. victim, lawyer, police, the software will supply to the user's needs.

* Victim:
   * Our software will allow the victim (user) to lodge FIR with the police online
     without having to visit the police station.If victim needs police for his case then he will be shown
     the police station nearer to his location.If the victim requires a lawyer then he can view the list
     of registered lawyers. He will be shown the lawyers previous record and will be informed about their 
     fees. Depending on which he can choose the lawyer of his choice.

* Lawyer:
   * The lawyer on logging in will be shown the status of all the cases he is concerned
     with. It will show him the dates of the next court hearings for his different cases.
     He will be able to accept and reject any new cases.
      
* Police:
    * The police will be shown the list of FIRs filed with their police station and the
      status of various cases. They can see the description of the case as given by the
      victim. It will show the policemen involved in that case and various other details.
      
## Work remaining
- Particulary in the case of lawyer we have to add some code that lawyer can update each case details day by day(like next hearing   date,what's the progess in the case etc..),so that victim can get all the details about case at his place.

- Same in the case of police(like lawyer)

- To improve the UI.
      
## Prerequisites
Django, Python3

### How to run the application
1. Clone the repository
> ``` https://github.com/pockemon/Online-Judiciary-System-OJS-```
2. Change directory
> ``` cd Online-Judiciary-System-OJS-```
3. Run the server
> ``` python manage.py runserver```
 
## License
The software is under MIT License

## Contributers
- Hardik Rana ([@Pockemon](https://github.com/Pockemon))
- Harshal Shinde ([@harshal9999](https://github.com/harshal9999))

