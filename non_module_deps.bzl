load(
  "@bazel_tools//tools/build_defs/repo:local.bzl",
  "local_repository",
  "new_local_repository",
)
load(
  "@bazel_tools//tools/build_defs/repo:git.bzl",
  "git_repository",
  "new_git_repository",
)
# -- load statements -- #

def _non_module_deps_impl(ctx):
  git_repository(
      name = "com_github_google_flatbuffers",
      remote = "https://github.com/google/flatbuffers.git",
      commit = "a2cd1ea3b6d3fee220106b5fed3f7ce8da9eb757",
  )
  new_git_repository(
      name = "kineto",
      remote = "https://github.com/pytorch/kineto.git",
      commit = "5e7501833f1021ce6f618572d3baf657b6319658",
      build_file = "//third_party:kineto.BUILD",
  )
  new_git_repository(
      name = "tensorpipe",
      build_file = "//third_party:tensorpipe.BUILD",
      remote = "https://github.com/pytorch/tensorpipe.git",
      commit = "52791a2fd214b2a9dc5759d36725909c1daa7f2e",
      recursive_init_submodules = True,
  )
  new_git_repository(
      name = "fbgemm",
      remote = "https://github.com/pytorch/fbgemm",
      commit = "157e88b750c452bef2ab4653fe9d1eeb151ce4c3",
      build_file = "//third_party:fbgemm/BUILD.bazel",
  )
  local_repository(
    name = "com_google_protobuf",
    path = "third_party/protobuf",
  )
  new_git_repository(
      name = "cudnn_frontend",
      build_file = "//third_party:cudnn_frontend.BUILD",
      remote = "https://github.com/NVIDIA/cudnn-frontend.git",
      commit = "f937055efc6d414d11f4c6577e3977fe74f35fb6",
  )
  new_git_repository(
      name = "ideep",
      remote = "https://github.com/intel/ideep",
      commit = "719d8e6cd7f7a0e01b155657526d693acf97c2b3",
      build_file = "//third_party:ideep.BUILD",
  )
  new_git_repository(
      name = "mkl_dnn",
      remote = "https://github.com/oneapi-src/oneDNN.git",
      commit = "8d263e693366ef8db40acc569cc7d8edf644556d",
      build_file = "//third_party:mkl-dnn.BUILD",
  )
  new_git_repository(
      name = "sleef",
      remote = "https://github.com/shibatch/sleef",
      commit = "5a1d179df9cf652951b59010a2d2075372d67f68",
      build_file = "//third_party:sleef.BUILD",
  )
  new_git_repository(
      name = "asmjit",
      remote = "https://github.com/asmjit/asmjit.git",
      commit = "e5d7c0bd5d9aec44d68830187138149e6a8c4e32",
      build_file = "//third_party:fbgemm/external/asmjit.BUILD",
  )
  new_git_repository(
      name = "org_pytorch_cpuinfo",
      remote = "https://github.com/pytorch/cpuinfo.git",
      commit = "5e3d2445e6a84d9599bee2bf78edbb4d80865e1d",
      build_file = "//third_party:cpuinfo/BUILD.bazel",
  )
  new_git_repository(
      name = "moodycamel",
      remote = "https://github.com/cameron314/concurrentqueue.git",
      commit = "c68072129c8a5b4025122ca5a0c82ab14b30cb03",
      build_file = "//third_party:moodycamel.BUILD",
  )
  new_git_repository(
      name = "cpuinfo",
      remote = "https://github.com/pytorch/cpuinfo.git",
      commit = "5e3d2445e6a84d9599bee2bf78edbb4d80865e1d",
      build_file = "//third_party:cpuinfo/BUILD.bazel",
  )

# -- repo definitions -- #

non_module_deps = module_extension(implementation = _non_module_deps_impl)
