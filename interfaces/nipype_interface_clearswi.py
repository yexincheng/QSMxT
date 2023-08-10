from nipype.interfaces.base import CommandLine, TraitedSpec, File, CommandLineInputSpec, traits, InputMultiPath
from scripts import qsmxt_functions
import os


class ClearSwiInputSpec(CommandLineInputSpec):
    phase = InputMultiPath(
        exists=True,
        mandatory=True,
        argstr="--phase %s"
    )
    magnitude = InputMultiPath(
        exists=True,
        mandatory=True,
        argstr="--magnitude %s"
    )
    TEs = traits.ListFloat(
        mandatory=False,
        argstr="--TEs '[%s]'"
    )
    TE = traits.Float(
        mandatory=False,
        argstr="--TEs '[%s]'"
    )
    swi = File(
        argstr="--swi-out %s",
        name_source=['phase'],
        name_template='%s_swi.nii'
    )
    swi_mip = File(
        argstr="--mip-out %s",
        name_source=['phase'],
        name_template='%s_swi-mip.nii'
    )

class ClearSwiOutputSpec(TraitedSpec):
    swi = File()
    swi_mip = File()

class ClearSwiInterface(CommandLine):
    input_spec = ClearSwiInputSpec
    output_spec = ClearSwiOutputSpec
    _cmd = os.path.join(qsmxt_functions.get_qsmxt_dir(), "scripts", "mrt_clearswi.jl")

    def _format_arg(self, name, trait_spec, value):
        if name == 'TEs' or name == 'TE':
            if self.inputs.TEs is None and self.inputs.TE is None:
                raise ValueError("Either TEs or TE must be provided")
        return super(ClearSwiInterface, self)._format_arg(name, trait_spec, value)

