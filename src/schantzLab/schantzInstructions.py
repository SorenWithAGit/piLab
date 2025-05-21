"""
#######################################################################
schantzInstructions.py is module within the schantzLab subfolder of
the pyLab package. 
This module contains classes with dictionaries containing the SOP
protocols for the Schantz Group.
#######################################################################
"""

class LAI:
    sop = """Plug in the instrument and toggle the silver
switch to "On". Start the lamp by pushing in the black
switch. 
Clean the belt with ethanol and kimwipes.
Run the silver calibration plate through the instrument.
Area should read 50 cm squared. Adjust the calibration screw
with a screwdriver until area is acceptable.
When ready to begin measurement press the reset button.
Place the sample on the belt and gently feed it until
the belt can support the sample. 
Once sample has passed the light bar record LAI.
Clean belt as described above.
Load next sample.
When all samples are completed toggle the power switch
and unplug the meter.
"""

class VarioMax:

    sop = {
        "Startup" : """Start-up
Open the argon and oxygen cylinders. 
On the right side of the Instrument push the green button.
Launch the Vario Max Cube Software, and enter password.
If instrument is in sleep mode:
press options -> settings -> sleep/wakeup press
wake up now.
Wait for startup sequence to complete, instrument arm
will move. Status will say standby when ready.
On the ribbon press options -> settings -> paramaters.
Set the combustion and post combustion tubes to 900 C.
Reduction tube to 830 C.
Allow the instrument to reach operating temp.""",
    
    "Sequence" : """Sample Sequence Setup
Begin the sequence with two blanks Method should be
Blank O2, weight should be input as 1.000. 
Add two "RunIn" samples comprised of aspartic acid
target weight of 100 mg.
Add three "aspartic acid" (type name) samples again
target weight is 100 mg. Method will be aspartic acid 1.
Begin adding sample info to the queue with a standard
every 10-20 samples.
For plant samples method is ?Plant?.
For soil samples method is ?Soil?.""",

    "Analysis" : """Analysis
Load the autosampler with samples input in the table.
If the Instrument has not been run in a while, it is
recommended to do the blanks and RunIn samples as 
single analysis (located on the ribbon menu).
If the blanks return low values and the RunIn's 
values are acceptable begin Auto-Analysis (ribbon).
Otherwise Auto-Analysis can be selected.
After the run has completed the instrument will enter
sleep mode. Close the valves on the supply tanks."""
    }

class rootScanner:

    sop = {
    "Root Processing" : """Root Processing
Place the sample in a 2mm soil sieve and shake to
remove excess loose soil.
With a secondary container below the sieve wash
the sample with water from the tap to remove 
remaining soil. 
For large root structures, cut sample into 
segments (select "Segment Example").
Collect fine roots that may have passed through
the sieve. 
Lay roots as flat as possible in sample tray.""",

    "Setup" : """Setup
Connect scanner and insert Regent USB key into
the computer, Turn on the root scanner.
On the computer open "WinRHIZO Reg 2022b" Folder.
If the run will use the same settings as the 
previous run, select "The same as the last time".
Select Epson Perfection V800/850 from the 
"Select Source" popup.
At the top ribbon click Image -> Aquisition
Parameters. Ensure Reagent Postioning System
matches the tray/spacers in scanner.
Adjust the margins according to the correct
calibration values.
Tray and spacers should be aligned to the top
right of the scanner window (Arrow).""",

    "Scanning" : """Scanning
At the left ribbon of WinRHIZO, click the
Scanner Icon to scan an image.
Shrink/enlarge the image via the magnification
option at the bottom left.
To select entire image for analysis, click
anywhere on the scan image. Click and drag
to analyze smaller areas.
Enter sample ID, soil volume, and operator,
click OK.
If running a new sample set click "Create One"
when prompted to create a txt file.
Name the file; subsequent scans will save
as new entries in text file.
If running an existing sample set click 
"Open one" and choose the corresponding file.
Setup next sample, align, scan and save as
new ID for remaining samples.""",

    "XLRhizo" : """XLRhizo and Exporting
In the main WinRHIZO folder open "XLRhizo 2022"
folder and open "XLRhizo.xlsx".
Enable macros.
At the top ribbon, click Add-ins -> XLRhizo ->
Open a WinRHIZO data file. Locate the text 
file from the scanned run and press ok.
Root data begins on column P.
Save as new file with sampleset name.
Do not save the XLRhizo file.
Eject the Regent USB key and return to
the WinRHIZO Supplies drawer."""
    }