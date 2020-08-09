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
