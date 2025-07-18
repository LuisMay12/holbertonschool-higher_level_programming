import os

def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process and generate output files, one for each attendee
    for idx, attendee in enumerate(attendees, start=1):
        output = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            output = output.replace(f"{{{key}}}", str(value) if value else "N/A")

        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
