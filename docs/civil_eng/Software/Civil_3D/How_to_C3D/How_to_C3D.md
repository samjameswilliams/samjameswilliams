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

## Workflow to create planar surface in arbitrary shaped area  

In the area below I wish to create a fall with a constant gradient. Basically a planar 
surface, constant intervals between parallel contours.

![Polyline_for_area](image.png)  

To ensure I can create a grading which will not interact with any other drawing objects
I create a new site.

![create_new_site_step_1](image-1.png)

![create_new_site_step_2](image-2.png)

I create a Featureline from the polyline.

![Featureline_from_poly](image-3.png)

Make sure you place the new Featureline in the Site you created.

![create_Featureline_dialogue](image-4.png)

In this example I want the top edge of the area to be 47.750 mAOD so I have a 
Polyline which is wider than the area I want to grade along the top edge.

![top_edge_Polyline](image-5.png)

I also turn this into a Featureline and add to a different site (to avoid interaction with the border Featureline) but this time I
select Grading Line for the Style (not sure if you need to but think you might),
and "Assign elevations" is ticked.

![top_edge_Featureline](image-6.png)  

![TSR_Village_South_grading_site](image-7.png)

![create_top_edge_featureline](image-8.png)

For this example I want the line to be a consistent level but you can see you 
have other options available to get elevations from gradings or surfaces too.  

![Assign_elevations](image-9.png)

Having done this you can now create a grading from it.

![Grading_creation](image-10.png)  

Ensure the desired site is selected and options are selected.

![Grading_group](image-11.png)

For me, I have a gradient in mind so I select the option to create a grading at a specific slope for a specific distance on plan.

![Create_grading](image-12.png)

Once you click the Create Grading button you select the Featureline and follow the prompts.

![Select_the_feature](image-13.png)

![Select_the_grading_side](image-14.png)

![Apply_to_entire_length](image-15.png)

![Distance](image-16.png)

![Slope](image-18.png)

!!! note

    * Positive numbers will mean your starting point is at the bottom of the slope and the grading slopes upwards, negative numbers mean your starting point is at the top and your grading slopes downwards.  
    * Gradients are written the opposite way around to common convention. So in this example -1:40 is -40:1 

 The grading is now created in the "TSR Village South Grading" Site.

 ![Grading](image-17.png)  

If you select the Featureline which makes the boundary you can open the Elevation editor. Using SHIFT select you can highlight all the Stations and then click "Elevations from Surface"

![Elevation_editor](image-19.png)

![Set_elevations_from_surface](image-20.png)

To check the boundary Featureline has the right elevations you can add Contour labels 

![Annotate_Contour_multiple](image-21.png)

![Spot_check](image-22.png)

Create a new Surface for the slab.

![Create_new_surface](image-24.png)

![TSR_Village_South](image-25.png)

With the Featureline selected you right click and "Add to Surface as Breakline"

![Add_to_surface_as_breakline](image-23.png)

![Add_to_TSR_Village_South](image-26.png)

This hasn't created the surface as desired because there are no stations on the Arc.  To add some, re-open the Elevation Editor.

![Add_stations](image-27.png)

These will also need to be moved onto the surface. So follow the same procedure as before.

!!! note

    This could probably be avoided by converting the arc to lines while it is still a polyline before making it into a Featureline.

![Add_user_stations_to_surface](image-28.png)

![Rebuild](image-29.png)

In order to see the new surface it is helpful to not display the grading used to set the elevations in the new slab.

![No_display](image-30.png)

This shows that the re-entrant corners of the new slab are infilled. This isn't what we want

![Re-entrant_infill](image-31.png)

To sort this out the Featureline can be added to the Surface as a Boundary.

![Add_boundary](image-32.png)

![Add_boundaries_window](image-33.png)

And there it is.

![Finished_slab](image-34.png)
