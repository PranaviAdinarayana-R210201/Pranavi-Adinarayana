clc
clear all
close all
t=0:0.01:1
F1=4
F2=2
x1=cos(2*pi*F1*t)
x2=cos(2*pi*F2*t)
m=x1+x2
plot(m)