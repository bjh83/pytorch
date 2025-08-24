load("@rules_python//python/pip_install:pip_repository.bzl", "pip_repository")
# -- load statements -- #

def _extension_for_pip_repository_impl(ctx):
  pip_repository(
    name = "pip_deps",
    requirements_lock = "//:tools/build/bazel/requirements.txt",
    python_interpreter_target = "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
  )
  pip_repository(
    name = "pip_deps",
    requirements_lock = "//:tools/build/bazel/requirements.txt",
    python_interpreter_target = "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
  )
# -- repo definitions -- #

extension_for_pip_repository = module_extension(implementation = _extension_for_pip_repository_impl)
