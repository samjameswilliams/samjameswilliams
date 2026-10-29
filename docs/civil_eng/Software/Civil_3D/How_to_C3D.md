# How to do various things in Civil 3D

This page is to record useful links and step by step guides for things I think might be
hard to remember.

## Contour labels  

How to change the accuracy of contour labels is definitely not obvious but there's a 
great video showing you all the obscure clicks needed [here](https://screencast.autodesk.com/Embed/Timeline/c73c7a51-43d1-4eb2-b550-72207c7d80e6) ([original thread](https://forums.autodesk.com/t5/civil-3d-forum/contour-label-precision/td-p/6209528)).

## Triangulation

I never like seeing triangulation surfaces on finished drawings. But when you're trying to get a surface to just the shape you want it's often really useful to have the triangulation lines showing. 

## Breaklines

If you create a Feature line and make it a Grading line you can add it to a surface as a Breakline which means that triangulation lines won't cross it. That is, unless you have other Breaklines too close which make it impossible not to cross one or the other. 

## Sites for separation

I was getting confused why when I created new gradings they interacted with other objects in the drawing. I found that if you need objects to behave completely independently you should create a new "Site" for them. Once created you can use them to pull points on other objects to the same level as the new grading/surface. This can be useful if you want to impose a planar surface as part of a surface made of an irregular grid (i.e. you can get an area with curved contours to have parallel equidistant contours).



