#Initial codes
ny = read.csv('new_york_city.csv')
wash = read.csv('washington.csv')
chi = read.csv('chicago.csv')

head(ny)

head(wash)

head(chi)


#Question 1
#Using the data on Chicago, create a binary plot using ggplot with Start.Time as x axis and Trip.Duration as y axis. The y axis should range from 0 to 24,000. What are your observations?
# To load ggplot2
library(ggplot2)

#The ploting code for answering the question
p <- ggplot(aes(x =Start.Time, y= Trip.Duration), data=chi)

p +
  geom_point(aes(colour = Gender)) +
    ggtitle('Nexus Between Start Time and Trip Duration')+
  scale_colour_manual(values = c("orange", "forestgreen", "blue")) +
  coord_cartesian(ylim=c(0,24000))

#To present relevant summary statistics
summary(chi$Trip.Duration)
by(chi$Trip.Duration, chi$Gender, summary)

#Summary of your question 1 results goes here. The result (on Chicago) projects the relationship between the trip duration and the start time, separated based on gender. The data diagram shows the results including the NA which are coloured as yellow. Majority of the NA datasets are results above 5000 trip duration. On avregare, femeles have the higher trip duration in Chicago.


#Question 2
#Your question 2 goes here. Create a hostogram of Trip Duration in Ney York City based on Gender (include NA results also) and limit it to a count of 5,000 Trips. What gender has the highest trip duration?
# To load ggplot2
library(ggplot2)

#The ploting code for answering the question
ggplot(aes(x=Trip.Duration), data=subset(ny, !is.na(Gender)))+
    geom_histogram(binwidth=10)+
    ggtitle('Histogram of Trip Durations')+
    labs(x='Trip Duration')+
    scale_x_continuous(limits=c(0,5000))+
    facet_wrap(~Gender)

#To present relevant summary statistics
table(ny$Gender)
by(ny$Trip.Duration, ny$Gender, summary)

#Summary of your question 2 results goes here. The graph shows that males have more data as compared to females. However, the counts are concentrated below a trip duration of 2000. Thus, the average duration of females, 876 is higher than that of males, 768.9.
