from fiona import collection

def read_text(filename):
    """Read a text file and return a list of rows

    Args:
        filename(str): path to file to open

    Returns:
        List of lines from text file

    """
    with open(filename,"r") as lines:
        return lines.readlines()

def write_shape(filename,schema,data):
    """Write to filename based on schema as ESRI shapefile

    Args:
    filename(str) : path to output
    schema(dict) data schema
    data(list) list of dicts with data
    """
    with collection(filename,"w", "ESRI Shapefile", schema) as output:
        for row in data:
            output.write(row)

