load(
  "@bazel_tools//tools/build_defs/repo:local.bzl",
  "local_repository",
  "new_local_repository",
)
# -- load statements -- #

def _non_module_deps_impl(ctx):
  local_repository(
      name = "com_github_google_flatbuffers",
      path = "third_party/flatbuffers",
  )
  new_local_repository(
      name = "kineto",
      build_file = "//third_party:kineto.BUILD",
      path = "third_party/kineto",
  )
  new_local_repository(
      name = "tensorpipe",
      build_file = "//third_party:tensorpipe.BUILD",
      path = "third_party/tensorpipe",
  )
  new_local_repository(
      name = "fbgemm",
      build_file = "//third_party:fbgemm/BUILD.bazel",
      path = "third_party/fbgemm",
  )
  local_repository(
    name = "com_google_protobuf",
    path = "third_party/protobuf",
  )
  new_local_repository(
      name = "cudnn_frontend",
      build_file = "//third_party:cudnn_frontend.BUILD",
      path = "third_party/cudnn_frontend/",
  )
  new_local_repository(
      name = "ideep",
      build_file = "//third_party:ideep.BUILD",
      path = "third_party/ideep",
  )
  new_local_repository(
      name = "mkl_dnn",
      build_file = "//third_party:mkl-dnn.BUILD",
      path = "third_party/ideep/mkl-dnn",
  )
  new_local_repository(
      name = "sleef",
      build_file = "//third_party:sleef.BUILD",
      path = "third_party/sleef",
  )
  new_local_repository(
      name = "asmjit",
      build_file = "//third_party:fbgemm/external/asmjit.BUILD",
      path = "third_party/fbgemm/external/asmjit",
  )
  new_local_repository(
      name = "org_pytorch_cpuinfo",
      build_file = "//third_party:cpuinfo/BUILD.bazel",
      path = "third_party/cpuinfo",
  )
  new_local_repository(
      name = "moodycamel",
      build_file = "//third_party:moodycamel.BUILD",
      path = "third_party/concurrentqueue",
  )
  new_local_repository(
      name = "cpuinfo",
      path = "third_party/cpuinfo",
      build_file = "//third_party:cpuinfo/BUILD.bazel",
  )

# -- repo definitions -- #

non_module_deps = module_extension(implementation = _non_module_deps_impl)
