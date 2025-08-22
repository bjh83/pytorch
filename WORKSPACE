workspace(name = "pytorch")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
load("//tools/rules:workspace.bzl", "new_patched_local_repository")

http_archive(
    name = "rules_cc",
    patches = [
        "//:tools/rules_cc/cuda_support.patch",
    ],
    strip_prefix = "rules_cc-40548a2974f1aea06215272d9c2b47a14a24e556",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_cc/archive/40548a2974f1aea06215272d9c2b47a14a24e556.tar.gz",
        "https://github.com/bazelbuild/rules_cc/archive/40548a2974f1aea06215272d9c2b47a14a24e556.tar.gz",
    ],
)

http_archive(
    name = "rules_cuda",
    strip_prefix = "runtime-b1c7cce21ba4661c17ac72421c6a0e2015e7bef3/third_party/rules_cuda",
    urls = ["https://github.com/tensorflow/runtime/archive/b1c7cce21ba4661c17ac72421c6a0e2015e7bef3.tar.gz"],
)

http_archive(
    name = "platforms",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.10/platforms-0.0.10.tar.gz",
        # TODO Fix bazel linter to support hashes for release tarballs.
        # "https://github.com/bazelbuild/platforms/releases/download/0.0.10/platforms-0.0.10.tar.gz",
    ],
    # sha256 = "218efe8ee736d26a3572663b374a253c012b716d8af0c07e842e82f238a0a7ee",
)

load("@rules_cuda//cuda:dependencies.bzl", "rules_cuda_dependencies")

rules_cuda_dependencies(with_rules_cc = False)

load("@rules_cc//cc:repositories.bzl", "rules_cc_toolchains")

rules_cc_toolchains()

http_archive(
    name = "bazel_skylib",
    urls = [
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.0.2/bazel-skylib-1.0.2.tar.gz",
    ],
)

http_archive(
    name = "pybind11_bazel",
    strip_prefix = "pybind11_bazel-b162c7c88a253e3f6b673df0c621aca27596ce6b",
    urls = ["https://github.com/pybind/pybind11_bazel/archive/b162c7c88a253e3f6b673df0c621aca27596ce6b.zip"],
)

git_repository(
    name = "pybind11",
    build_file = "@pybind11_bazel//:pybind11.BUILD",
    remote = "https://github.com/pybind/pybind11.git",
    commit = "a2e59f0e7065404b44dfe92a28aca47ba1378dc4",
)

http_archive(
    name = "com_github_glog",
    build_file_content = """
licenses(['notice'])

load(':bazel/glog.bzl', 'glog_library')
# TODO: figure out why enabling gflags leads to SIGSEV on the logging init
glog_library(with_gflags=0)
    """,
    strip_prefix = "glog-0.4.0",
    urls = [
        "https://github.com/google/glog/archive/v0.4.0.tar.gz",
    ],
)

http_archive(
    name = "com_github_gflags_gflags",
    strip_prefix = "gflags-2.2.2",
    urls = [
        "https://github.com/gflags/gflags/archive/v2.2.2.tar.gz",
    ],
)

http_archive(
    name = "com_github_opentelemetry-cpp",
    urls = [
        "https://github.com/open-telemetry/opentelemetry-cpp/archive/refs/tags/v1.14.2.tar.gz",
    ],
)

git_repository(
    name = "gloo",
    build_file = "//third_party:gloo.BUILD",
    remote = "https://github.com/pytorch/gloo",
    commit = "c7b7b022c124d9643957d9bd55f57ac59fce8fa2",
)

git_repository(
    name = "onnx",
    build_file = "//third_party:onnx.BUILD",
    remote = "https://github.com/onnx/onnx.git",
    commit = "e709452ef2bbc1d113faf678c24e6d3467696e83",
)

git_repository(
    name = "com_google_protobuf",
    remote = "https://github.com/protocolbuffers/protobuf.git",
    commit = "d1eca4e4b421cd2997495c4b4e65cea6be4e9b8a",
)

http_archive(
    name = "eigen",
    build_file = "//third_party:eigen.BUILD",
    url = "https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.zip",
)

git_repository(
    name = "cutlass",
    build_file = "//third_party:cutlass.BUILD",
    remote = "https://github.com/NVIDIA/cutlass.git",
    commit = "b995f933179c22d3fe0d871c3a53d11e4681950f",
)

git_repository(
    name = "fbgemm",
    remote = "https://github.com/pytorch/fbgemm",
    commit = "157e88b750c452bef2ab4653fe9d1eeb151ce4c3",
    repo_mapping = {"@cpuinfo": "@org_pytorch_cpuinfo"},
)

git_repository(
    name = "ideep",
    build_file = "//third_party:ideep.BUILD",
    remote = "https://github.com/intel/ideep",
    commit = "719d8e6cd7f7a0e01b155657526d693acf97c2b3",
)

new_local_repository(
    name = "mkl_dnn",
    build_file = "//third_party:mkl-dnn.BUILD",
    path = "third_party/ideep/mkl-dnn",
)

git_repository(
    name = "org_pytorch_cpuinfo",
    remote = "https://github.com/pytorch/cpuinfo.git",
    commit = "5e3d2445e6a84d9599bee2bf78edbb4d80865e1d",
)

new_local_repository(
    name = "asmjit",
    build_file = "//third_party:fbgemm/external/asmjit.BUILD",
    path = "third_party/fbgemm/external/asmjit",
)

git_repository(
    name = "sleef",
    build_file = "//third_party:sleef.BUILD",
    remote = "https://github.com/shibatch/sleef",
    commit = "5a1d179df9cf652951b59010a2d2075372d67f68",
)

git_repository(
    name = "fmt",
    build_file = "//third_party:fmt.BUILD",
    remote = "https://github.com/fmtlib/fmt.git",
    commit = "40626af88bd7df9a5fb80be7b25ac85b122d6c21",
)

new_local_repository(
    name = "kineto",
    build_file = "//third_party:kineto.BUILD",
    path = "third_party/kineto",
)

git_repository(
    name = "opentelemetry-cpp",
    build_file = "//third_party:opentelemetry-cpp.BUILD",
    remote = "https://github.com/open-telemetry/opentelemetry-cpp.git",
    commit = "a799f4aed9c94b765dcdaabaeab7d5e7e2310878",
)

git_repository(
    name = "cpp-httplib",
    build_file = "//third_party:cpp-httplib.BUILD",
    remote = "https://github.com/yhirose/cpp-httplib.git",
    commit = "3af7f2c16147f3fbc6e4d717032daf505dc1652c",
)

git_repository(
    name = "nlohmann",
    build_file = "//third_party:nlohmann.BUILD",
    remote = "https://github.com/nlohmann/json.git",
    commit = "55f93686c01528224f448c19128836e7df245f72",
)

new_local_repository(
    name = "moodycamel",
    build_file = "//third_party:moodycamel.BUILD",
    path = "third_party/concurrentqueue",
)

git_repository(
    name = "tensorpipe",
    build_file = "//third_party:tensorpipe.BUILD",
    remote = "https://github.com/pytorch/tensorpipe.git",
    commit = "52791a2fd214b2a9dc5759d36725909c1daa7f2e",
    recursive_init_submodules = True,
)

http_archive(
    name = "mkl",
    build_file = "//third_party:mkl.BUILD",
    sha256 = "59154b30dd74561e90d547f9a3af26c75b6f4546210888f09c9d4db8f4bf9d4c",
    strip_prefix = "lib",
    urls = [
        "https://anaconda.org/anaconda/mkl/2020.0/download/linux-64/mkl-2020.0-166.tar.bz2",
    ],
)

http_archive(
    name = "mkl_headers",
    build_file = "//third_party:mkl_headers.BUILD",
    sha256 = "2af3494a4bebe5ddccfdc43bacc80fcd78d14c1954b81d2c8e3d73b55527af90",
    urls = [
        "https://anaconda.org/anaconda/mkl-include/2020.0/download/linux-64/mkl-include-2020.0-166.tar.bz2",
    ],
)

http_archive(
    name = "rules_python",
    # TODO Fix bazel linter to support hashes for release tarballs.
    #
    # sha256 = "94750828b18044533e98a129003b6a68001204038dc4749f40b195b24c38f49f",
    strip_prefix = "rules_python-0.21.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3_10",
    python_version = "3.10",
)

load("@python3_10//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip_deps",
    python_interpreter_target = interpreter,
    requirements_lock = "//:tools/build/bazel/requirements.txt",
)

load("@pip_deps//:requirements.bzl", "install_deps")

install_deps()

load("@pybind11_bazel//:python_configure.bzl", "python_configure")

python_configure(
    name = "local_config_python",
    python_interpreter_target = interpreter,
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

new_local_repository(
    name = "cuda",
    build_file = "@//third_party:cuda.BUILD",
    path = "/usr/local/cuda",
)

http_archive(
    name = "cudnn",
    build_file = "@//third_party:cudnn.BUILD",
    strip_prefix = "cudnn-linux-x86_64-9.12.0.46_cuda12-archive",
    url = "https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-9.12.0.46_cuda12-archive.tar.xz",
)

git_repository(
    name = "cudnn_frontend",
    build_file = "@//third_party:cudnn_frontend.BUILD",
    remote = "https://github.com/NVIDIA/cudnn-frontend.git",
    commit = "f937055efc6d414d11f4c6577e3977fe74f35fb6",
)

git_repository(
    name = "com_github_google_flatbuffers",
    remote = "https://github.com/google/flatbuffers.git",
    commit = "a2cd1ea3b6d3fee220106b5fed3f7ce8da9eb757",
)

git_repository(
    name = "google_benchmark",
    remote = "https://github.com/google/benchmark.git",
    commit = "299e5928955cc62af9968370293b916f5130916f",
)

git_repository(
    name = "com_google_googletest",
    remote = "https://github.com/google/googletest.git",
    commit = "52eb8108c5bdec04579160ae17225d66034bd723",
)

git_repository(
    name = "pthreadpool",
    remote = "https://github.com/Maratyszcza/pthreadpool.git",
    commit = "4fe0e1e183925bf8cfa6aae24237e724a96479b8",
    repo_mapping = {"@com_google_benchmark": "@google_benchmark"},
)

git_repository(
    name = "FXdiv",
    remote = "https://github.com/Maratyszcza/FXdiv.git",
    commit = "b408327ac2a15ec3e43352421954f5b1967701d1",
    repo_mapping = {"@com_google_benchmark": "@google_benchmark"},
)

git_repository(
    name = "XNNPACK",
    remote = "https://github.com/google/XNNPACK.git",
    commit = "51a0103656eff6fc9bfd39a4597923c4b542c883",
    repo_mapping = {"@com_google_benchmark": "@google_benchmark"},
)

git_repository(
    name = "gemmlowp",
    remote = "https://github.com/google/gemmlowp.git",
    commit = "3fb5c176c17c765a3492cd2f0321b0dab712f350",
)

git_repository(
    name = "kleidiai",
    repo_mapping = {"@com_google_googletest": "@com_google_benchmark"},
    remote = "https://github.com/ARM-software/kleidiai.git",
    commit = "cca02c2f69dd18e1f12647c1c0bdc8cf90e680c7",
)

### Unused repos start

# `unused` repos are defined to hide bazel files from submodules of submodules.
# This allows us to run `bazel build //...` and not worry about the submodules madness.
# Otherwise everything traverses recursively and a lot of submodules of submodules have
# they own bazel build files.

local_repository(
    name = "unused_tensorpipe_googletest",
    path = "third_party/tensorpipe/third_party/googletest",
)

local_repository(
    name = "unused_fbgemm",
    path = "third_party/fbgemm",
)

local_repository(
    name = "unused_ftm_bazel",
    path = "third_party/fmt/support/bazel",
)

local_repository(
    name = "unused_kineto_fmt_bazel",
    path = "third_party/kineto/libkineto/third_party/fmt/support/bazel",
)

local_repository(
    name = "unused_kineto_dynolog_googletest",
    path = "third_party/kineto/libkineto/third_party/dynolog/third_party/googletest",
)

local_repository(
    name = "unused_kineto_dynolog_gflags",
    path = "third_party/kineto/libkineto/third_party/dynolog/third_party/gflags",
)

local_repository(
    name = "unused_kineto_dynolog_glog",
    path = "third_party/kineto/libkineto/third_party/dynolog/third_party/glog",
)

local_repository(
    name = "unused_kineto_googletest",
    path = "third_party/kineto/libkineto/third_party/googletest",
)

local_repository(
    name = "unused_onnx_benchmark",
    path = "third_party/onnx/third_party/benchmark",
)

### Unused repos end
