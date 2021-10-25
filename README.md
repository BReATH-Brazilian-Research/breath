# BReATH - Brazilian Research of Atmosphere Towards Health

BReATH project aims to create a interface to visualize and get insights relating asthma and weather data.

# Authors

- [233840, Elton Cardoso do Nascimento](https://github.com/EltonCN)
- [218733, João Pedro de Moraes Bonucci](https://github.com/Joao-Pedro-MB)
- [240106, Lucas Otávio Nascimento de Araújo](https://github.com/Lucas-Otavio)
- [244712, Thiago Danilo Silva de Lacerda](https://github.com/ThiagoDSL)

# Software architecture

Our software system is architected using C4 and UML diagrams. This repository contains the main application and service management, with other services separated across multiple repositorys, containing our different Python modules. It was divided in this way to help manage the different activities of the disciplines linked to this project.

_Imagem do diagrama PythonModules_
![]() 


## Context

_Texto explicando o contexto_

_Imagem do diagrama Contexto_
![]() 

## Container, components and code

Our container level describes our **service-oriented architecture**. Each service realizes a set of operations, and is isolated in a different Python process. 

Within the some containers section we also have the component and code level description. We describe only the main and already designed components of the architecture, as some are related to features not yet started.

_Imagem do diagrama Container_
![]() 

_Descrição da responsabilidade de cada componente/BD_
### Session Manager

This component orchestrates service requests, and handles the login session.

__Imagem do diagrama de componentes__
![]()


#### RequestSessionManager

Handles the lifecycle of a request, from receiving it to sending its response.

We used the [Chain of Responsibility](https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility) design pattern to create it, as can be seen on its code diagram. Because we use Python, which supports multiple inheritance, we use an abstract class, as there is no difference between it and an interface.

__Imagem do diagrama de código__
![]()



### BReATH Map and Patient Portal: 
### DataWorflow: 
### DataRequester: 
### Prediction: 
### BDAcessPoint: 

Description

- RequestProcesser:
- GraphQuerier
- RelationalQuerier

### Databases:
- SQL: 
- Graph: 



