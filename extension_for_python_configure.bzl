# extension_for_python_configure.bzl

def _local_cfg_impl(rctx):
    # Optional: point to your real CPython include dir at build time:
    #   --repo_env=PYTHON_INCLUDE=$(python3 -c 'import sysconfig;print(sysconfig.get_paths()["include"])')
    inc = rctx.os.environ.get("PYTHON_INCLUDE", "")

    lines = ["package(default_visibility=['//visibility:public'])"]

    if inc:
        # Make headers available under python_include/
        rctx.symlink(inc, "python_include")
        lines += [
            "cc_library(",
            "    name = 'python_headers',",
            "    hdrs = glob([",
            "        'python_include/**/*.h',",
            "        'python_include/**/*.hpp',",
            "        'python_include/**/*.hh',",
            "        'python_include/**/*.inc',",
            "    ]),",
            "    includes = ['python_include'],",
            ")",
            "alias(name = 'python_include', actual = ':python_headers')",
        ]
    else:
        # Empty C++ lib still provides CcInfo so deps work during analysis
        lines += [
            "cc_library(name = 'python_headers')",
            "alias(name = 'python_include', actual = ':python_headers')",
        ]

    # IMPORTANT: write real newlines, not escaped \n
    rctx.file("BUILD.bazel", "\n".join(lines) + "\n")

_local_config_python_repo = repository_rule(
    implementation = _local_cfg_impl,
    environ = ["PYTHON_INCLUDE"],
)

def _ext_impl(_ctx):
    _local_config_python_repo(name = "local_config_python")

extension_for_python_configure = module_extension(implementation = _ext_impl)

