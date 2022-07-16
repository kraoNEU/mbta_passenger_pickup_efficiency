# &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MBTA Passenger Pickup Efficiency

**MBTA** ([Massachusetts Bay Transport Authority](https://en.wikipedia.org/wiki/Massachusetts_Bay_Transportation_Authority)) is the public agency responsible for operating most public transportation services in Greater Boston, Massachusetts. It's Annual Ridership stands at 160 Million making it one of the most used, popular urban transport anywhere in the USA. From students to elders, nurses, and doctors, there is no doubt that the positive impact it has made is life changing. It is cheap, convenient, reaches most major hotspots, and is time friendly. With that being said, The MBTA has been running into a lot of service disruptions and cost-overruns for quite a while for numerous reasons.<br>

With Recent developments in technology in the domain of Data Science and Machine Learning, one can’t help but think: **How can we apply these advancements in Data Analysis to help make it more efficient, and reach full functionality.** One of the most effective methods is observing data channels such as hotspots, crowded stations, hours of the day, days of the week, and accordingly adjust timetables and/or routes to make the routes more efficient. Be it time, space, or energy, there are a lot of factors that go into making that decision. Essentially we will be conducting a data study where we hope to identify key "pain points" that could be addressed further to make it truly a world-class and efficient urban transportation service.

## Data Sources

**The Data is being taken from the MBTA's latest V3 API:**<br>

- [MBTA Documentation for V3 API](https://api-v3.mbta.com/docs/swagger/index.html)
- [MBTA V3 API key Request](https://api-v3.mbta.com/portal)
- [MBTA V3 API Website](https://www.mbta.com/developers/v3-api)

## Project partners

* Student #1 (identify partner by name -- the entire team should use this partner's github-classroom repo for the project)
* Student #2 (ditto)
* Student #3 (ditto)

## Goal

The project goal is to develop a predictive model for COVID-19 vaccine effectiveness 
at the county level based on death rate and possibly other socioeconomic factors.
We'll start by investigating the relationship between 
vaccination rate and death rate. 
We'll be careful to determine time-dependence, since vaccines were rolled out in May 2021 and 
probably had their maximum effectiveness the following November, as mentioned
in [this NPR story](https://www.npr.org/sections/health-shots/2021/12/05/1059828993/data-vaccine-misinformation-trump-counties-covid-death-rate), which is where we developed the idea for this project.

## Data

Primary sources of data will be CDC and Johns Hopkins university.

* [CDC](https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County)
* [Johns Hopkins](https://github.com/CSSEGISandData/COVID-19)

## Stakeholder

This could be a faculty member or someone from an organization with an interest in this problem who
would be willing to provide feedback on your prototypes.

## Preliminary result

The figure shows vaccination rate versus population for each county in the U.S. 
It was created using a CSV file downloaded from obtained from the CDC site listed above.

![](figs/fig1.png)

Recreate this figure with the following command:

```
python src/app.py
```

## Project plan

[plan.md](plan.md)

