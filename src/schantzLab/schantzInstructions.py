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

