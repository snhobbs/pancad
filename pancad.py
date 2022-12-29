import os
import click


def translate(in_f, out_f):
    import FreeCAD
    import Part, Mesh, App
    shape = Part.Shape()
    shape.read(in_f)
    doc = App.newDocument('Doc')
    pf = doc.addObject("Part::Feature","MyShape")
    pf.Shape = shape
    Mesh.export([pf], out_f)


@click.command()
@click.option("--in", "-i", "in_f", required=True, help="input file")
@click.option("--out", "-o", required=True, help="output file")
def main(in_f, out):
    _, in_format = os.path.splitext(in_f)
    _, out_format = os.path.splitext(out)
    translate(in_f, out)



if __name__ == "__main__":
    main()
