# Zero to Hero training notes

## Session 1: Creating and editing surfaces  

*Delivered by Carlos Aquise and Luis Hidalgo*  

Toolspace menu is likely to be where you'll access most of what you need. Objects are in the "Prospector", configuration is in the "Settings".  

C3D triangulation method ensures that every triangle can have all 3 points inscribed in a circle without inscribing points from another triangle 
(Triangular Irregular Surface [TIN]).

### Tips

Save file and georeference before doing anything else.

`Selection cycling = 2` allows you to cycle through to objects below your click

Always freeze your surveyed levels so you can't delete or modify them by accident.

`MAPCLEAN` alternative to `TRIM`. Includes option to convert Lines and Arcs to Polylines which you can join to get continuous polylines.

`_No_Display` style is useful for having objects in the drawing which are useful for reference but you don't want to see.  

In Surface Properties > Definition > Build you can do things like Exclude elevations above/below. Also exclude maximum triangle length, this can help with irregular shaped data (non-rectangular). This may accidentally exclude sparsely surveyed areas but you can modify the boundary and rebuild with the exclude option turned off/down.

Contour/spot level annotations are highly customisable. Annotation text can be added between dynamic fields.  

You can create custom text imports quite readily (example given was comma delimited Point nr, Northing, Easting, Elevation in .txt).

Adding surveys as a point group allows you to audit/verify. Keep it separate from the surface.

.dwg with exploded geometry and text is a little trickier.

SHIFT + right mouse brings up snaps if in the middle of a command.  

Move text to elevation moves text to the elevation of its text. 