resolved = [
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "bazel_tools",
               "path": "/home/brendan/.cache/bazel/_bazel_brendan/install/fa7424f9d9bea3343b34bddfb53e924e/embedded_tools"
          },
          "native": "local_repository(name = \"bazel_tools\", path = __embedded_dir__ + \"/\" + \"embedded_tools\")"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository build_bazel_apple_support instantiated at:\n  /home/brendan/pytorch/WORKSPACE:6:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "build_bazel_apple_support",
               "url": "https://github.com/bazelbuild/apple_support/releases/download/1.22.1/apple_support.1.22.1.tar.gz",
               "sha256": "6fe50a731bd31b4af3ad7bdefff19db47b36a684e55e4b9674a7af1401349eae"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/apple_support/releases/download/1.22.1/apple_support.1.22.1.tar.gz",
                         "urls": [],
                         "sha256": "6fe50a731bd31b4af3ad7bdefff19db47b36a684e55e4b9674a7af1401349eae",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "build_bazel_apple_support"
                    },
                    "output_tree_hash": "59d64905a6607a51cde0343de3c6a3d2262c21f2a87730fdad3d1043faada6f5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_features instantiated at:\n  /home/brendan/pytorch/WORKSPACE:17:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:59:11: in apple_support_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:29:18: in _maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_features",
               "generator_name": "bazel_features",
               "generator_function": "apple_support_dependencies",
               "generator_location": None,
               "url": "https://github.com/bazel-contrib/bazel_features/releases/download/v1.27.0/bazel_features-v1.27.0.tar.gz",
               "sha256": "2da0aaccbd725ad61f4e35d6d75ed421bf73ec1de167458b00ffecef3cd78f6d",
               "strip_prefix": "bazel_features-1.27.0"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazel-contrib/bazel_features/releases/download/v1.27.0/bazel_features-v1.27.0.tar.gz",
                         "urls": [],
                         "sha256": "2da0aaccbd725ad61f4e35d6d75ed421bf73ec1de167458b00ffecef3cd78f6d",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "bazel_features-1.27.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_features"
                    },
                    "output_tree_hash": "52e706ec6b29e4d2cc398b0eff0b27a52a7156f977070f261996a3170d9f8d13"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cuda instantiated at:\n  /home/brendan/pytorch/WORKSPACE:45:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cuda",
               "urls": [
                    "https://github.com/bazel-contrib/rules_cuda/releases/download/v0.2.5/rules_cuda-v0.2.5.tar.gz"
               ],
               "sha256": "fe8d3d8ed52b9b433f89021b03e3c428a82e10ed90c72808cc4988d1f4b9d1b3",
               "strip_prefix": "rules_cuda-v0.2.5"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazel-contrib/rules_cuda/releases/download/v0.2.5/rules_cuda-v0.2.5.tar.gz"
                         ],
                         "sha256": "fe8d3d8ed52b9b433f89021b03e3c428a82e10ed90c72808cc4988d1f4b9d1b3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_cuda-v0.2.5",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cuda"
                    },
                    "output_tree_hash": "08d6de579e4d86555221a61b717727c4f1de511b2dc75033143a8cc01fe966e5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_cc instantiated at:\n  /home/brendan/pytorch/WORKSPACE:17:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:67:11: in apple_support_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:29:18: in _maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_cc",
               "generator_name": "rules_cc",
               "generator_function": "apple_support_dependencies",
               "generator_location": None,
               "url": "https://github.com/bazelbuild/rules_cc/releases/download/0.0.8/rules_cc-0.0.8.tar.gz",
               "sha256": "ae46b722a8b8e9b62170f83bfb040cbf12adb732144e689985a66b26410a7d6f",
               "strip_prefix": "rules_cc-0.0.8"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_cc/releases/download/0.0.8/rules_cc-0.0.8.tar.gz",
                         "urls": [],
                         "sha256": "ae46b722a8b8e9b62170f83bfb040cbf12adb732144e689985a66b26410a7d6f",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_cc-0.0.8",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_cc"
                    },
                    "output_tree_hash": "c79a4b6516d6b4c86c833b47d7fb94e3552ee8a96f6140723ce212810d2bb4e8"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_python instantiated at:\n  /home/brendan/pytorch/WORKSPACE:238:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_python",
               "url": "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
               "strip_prefix": "rules_python-0.21.0"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
                         "urls": [],
                         "sha256": "",
                         "integrity": "sha256-lHUIKLGARFM+mKEpADtqaAASBAONxHSfQLGVskw49J8=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_python-0.21.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_python"
                    },
                    "output_tree_hash": "0e1a4b7b77391134eb1ed8079427c1fd92a4766b2ed0fbcac7af97cae7c87dcd"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository bazel_skylib instantiated at:\n  /home/brendan/pytorch/WORKSPACE:17:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:39:11: in apple_support_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:29:18: in _maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "bazel_skylib",
               "generator_name": "bazel_skylib",
               "generator_function": "apple_support_dependencies",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
                    "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz"
               ],
               "sha256": "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz",
                              "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.3.0/bazel-skylib-1.3.0.tar.gz"
                         ],
                         "sha256": "74d544d96f4a5bb630d465ca8bbcfe231e3594e5aae57e1edbf17a6eb3ca2506",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "bazel_skylib"
                    },
                    "output_tree_hash": "ea7c4298620705f0369110da5db3dec89df5ed43983fc85435f336e5fb95b3f9"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
          "definition_information": "Repository python3_10 instantiated at:\n  /home/brendan/pytorch/WORKSPACE:253:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/repositories.bzl:563:22: in python_register_toolchains\nRepository rule toolchain_aliases defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/private/toolchains_repo.bzl:163:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_10",
               "generator_name": "python3_10",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "python_version": "3.10.9",
               "user_repository_name": "python3_10"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchain_aliases",
                    "attributes": {
                         "name": "python3_10",
                         "generator_name": "python3_10",
                         "generator_function": "python_register_toolchains",
                         "generator_location": None,
                         "python_version": "3.10.9",
                         "user_repository_name": "python3_10"
                    },
                    "output_tree_hash": "80227b9a2af352cbbc75d2d8073a7a8732cb33189695f5ef9cffbb1b8ab4d512"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
          "definition_information": "Repository pip_deps instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:155:19: in pip_parse\nRepository rule pip_repository defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:612:33: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps",
               "generator_name": "pip_deps",
               "generator_function": "pip_parse",
               "generator_location": None,
               "requirements_lock": "//:tools/build/bazel/requirements.txt",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%pip_repository",
                    "attributes": {
                         "name": "pip_deps",
                         "generator_name": "pip_deps",
                         "generator_function": "pip_parse",
                         "generator_location": None,
                         "requirements_lock": "//:tools/build/bazel/requirements.txt",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "2aea504e7840fbffe583fbef462acdcdbd64749c28f7cef38ca226f1d9c10689"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pybind11_bazel instantiated at:\n  /home/brendan/pytorch/WORKSPACE:69:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pybind11_bazel",
               "urls": [
                    "https://github.com/pybind/pybind11_bazel/archive/b162c7c88a253e3f6b673df0c621aca27596ce6b.zip"
               ],
               "strip_prefix": "pybind11_bazel-b162c7c88a253e3f6b673df0c621aca27596ce6b"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/pybind/pybind11_bazel/archive/b162c7c88a253e3f6b673df0c621aca27596ce6b.zip"
                         ],
                         "sha256": "",
                         "integrity": "sha256-tyxbRBNbkNH/q6UeCCQL4LkXB6xgvqCLtNhLRzFiEbs=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "pybind11_bazel-b162c7c88a253e3f6b673df0c621aca27596ce6b",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "pybind11_bazel"
                    },
                    "output_tree_hash": "441b27c83886e95ecfbbbc586752603a3b3f604b3f1432797595b6bf10bdb660"
               }
          ]
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "com_google_protobuf",
               "path": "third_party/protobuf"
          },
          "native": "local_repository(name = \"com_google_protobuf\", path = \"third_party/protobuf\")"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository rules_java_builtin instantiated at:\n  /DEFAULT.WORKSPACE:12:36: in <toplevel>\nRepository rule local_repository defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_java_builtin",
               "path": "/home/brendan/.cache/bazel/_bazel_brendan/install/fa7424f9d9bea3343b34bddfb53e924e/rules_java"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "rules_java_builtin",
                         "path": "/home/brendan/.cache/bazel/_bazel_brendan/install/fa7424f9d9bea3343b34bddfb53e924e/rules_java"
                    },
                    "output_tree_hash": "23156af102e8441d4b3e5358092fc1dce333786289d48b1df6503ecb8c735cf3"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
          "definition_information": "Repository internal_platforms_do_not_use instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:153:6: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule local_repository defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/local.bzl:64:35: in <toplevel>\n",
          "original_attributes": {
               "name": "internal_platforms_do_not_use",
               "generator_name": "internal_platforms_do_not_use",
               "generator_function": "maybe",
               "generator_location": None,
               "path": "/home/brendan/.cache/bazel/_bazel_brendan/install/fa7424f9d9bea3343b34bddfb53e924e/platforms"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:local.bzl%local_repository",
                    "attributes": {
                         "name": "internal_platforms_do_not_use",
                         "generator_name": "internal_platforms_do_not_use",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "path": "/home/brendan/.cache/bazel/_bazel_brendan/install/fa7424f9d9bea3343b34bddfb53e924e/platforms"
                    },
                    "output_tree_hash": "db797f5ddb49595460e727f2c71af1b3adfed4d65132bbe31bd9d3a06bd95dba"
               }
          ]
     },
     {
          "original_rule_class": "local_repository",
          "original_attributes": {
               "name": "com_github_google_flatbuffers",
               "path": "third_party/flatbuffers"
          },
          "native": "local_repository(name = \"com_github_google_flatbuffers\", path = \"third_party/flatbuffers\")"
     },
     {
          "original_rule_class": "@@internal_platforms_do_not_use//host:extension.bzl%host_platform_repo",
          "definition_information": "Repository host_platform instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:165:6: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule host_platform_repo defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/internal_platforms_do_not_use/host/extension.bzl:51:37: in <toplevel>\n",
          "original_attributes": {
               "name": "host_platform",
               "generator_name": "host_platform",
               "generator_function": "maybe",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@internal_platforms_do_not_use//host:extension.bzl%host_platform_repo",
                    "attributes": {
                         "name": "host_platform",
                         "generator_name": "host_platform",
                         "generator_function": "maybe",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bb7732a410e479305fb8602fbfbe14a04e932eed9f8384852c03def646e87d5"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository platforms instantiated at:\n  /home/brendan/pytorch/WORKSPACE:17:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:49:11: in apple_support_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:29:18: in _maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "platforms",
               "generator_name": "platforms",
               "generator_function": "apple_support_dependencies",
               "generator_location": None,
               "urls": [
                    "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.9.tar.gz",
                    "https://github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.9.tar.gz"
               ],
               "sha256": "5eda539c841265031c2f82d8ae7a3a6490bd62176e0c038fc469eabf91f6149b"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://mirror.bazel.build/github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.9.tar.gz",
                              "https://github.com/bazelbuild/platforms/releases/download/0.0.9/platforms-0.0.9.tar.gz"
                         ],
                         "sha256": "5eda539c841265031c2f82d8ae7a3a6490bd62176e0c038fc469eabf91f6149b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "platforms"
                    },
                    "output_tree_hash": "567cadb959c1beeda065e093b6599dc3a3f7b8c41db40593f601b2c99830eb3d"
               }
          ]
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "pybind11",
               "path": "third_party/pybind11",
               "build_file": "@@pybind11_bazel//:pybind11.BUILD"
          },
          "native": "new_local_repository(name = \"pybind11\", path = \"third_party/pybind11\", build_file = Label(\"@@pybind11_bazel//:pybind11.BUILD\"))"
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bef508c068dd47d605f62c53ab0628f1f7f5101fdcc8ada09b2067b36c47931f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_toolchain_config_repo",
               "generator_name": "remotejdk11_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "d0587a4ecc9323d5cf65314b2d284b520ffb5ee1d3231cc6601efa13dadcc0f4"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "ca1d067909669aa58188026a7da06d43bdec74a3ba5c122af8a4c3660acd8d8f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b6a178fc0ca08a4473490f1c5d0f9f633db0ca0f2834c69dd08ce8290cf9ca86"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_macos_toolchain_config_repo",
               "generator_name": "remotejdk11_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_name": "remotejdk11_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "45b3b36d22d3e614745e7a5e838351c32fe0eabb09a4a197bac0f4d416a950ce"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0a170bf4f31e6c4621aeb4d4ce4b75b808be2f3a63cb55dc8172c27707d299ab"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_windows_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_windows_toolchain_config_repo",
               "generator_name": "remote_jdk8_windows_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_windows_toolchain_config_repo",
                         "generator_name": "remote_jdk8_windows_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_windows//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "8d0b08c18f215c185d64efe72054a5ffef36325906c34ebf1d3c710d4ba5c685"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "3272b586976beea589d09ea8029fd5d714da40127c8850e3480991c2440c5825"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk11_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c237bd9668de9b6437c452c020ea5bc717ff80b1a5ffd581adfdc7d4a6c5fe03"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
          "definition_information": "Repository python3_10_toolchains instantiated at:\n  /home/brendan/pytorch/WORKSPACE:253:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/repositories.bzl:556:20: in python_register_toolchains\nRepository rule toolchains_repo defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/private/toolchains_repo.bzl:76:34: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_10_toolchains",
               "generator_name": "python3_10_toolchains",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "python_version": "3.10.9",
               "set_python_version_constraint": False,
               "user_repository_name": "python3_10"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/private:toolchains_repo.bzl%toolchains_repo",
                    "attributes": {
                         "name": "python3_10_toolchains",
                         "generator_name": "python3_10_toolchains",
                         "generator_function": "python_register_toolchains",
                         "generator_location": None,
                         "python_version": "3.10.9",
                         "set_python_version_constraint": False,
                         "user_repository_name": "python3_10"
                    },
                    "output_tree_hash": "b819dffec84ae6805d952646a1f1e9e832bda1273e6d26d2f8780b2bbc669d3c"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_cc//cc/private/toolchain:cc_configure.bzl%cc_autoconf_toolchains",
          "definition_information": "Repository local_config_cc_toolchains instantiated at:\n  /home/brendan/pytorch/WORKSPACE:60:20: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cc/cc/repositories.bzl:10:17: in rules_cc_toolchains\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cc/cc/private/toolchain/cc_configure.bzl:144:27: in cc_configure\nRepository rule cc_autoconf_toolchains defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cc/cc/private/toolchain/cc_configure.bzl:47:41: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc_toolchains",
               "generator_name": "local_config_cc_toolchains",
               "generator_function": "rules_cc_toolchains",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@rules_cc//cc/private/toolchain:cc_configure.bzl%cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_cc_toolchains",
                         "generator_name": "local_config_cc_toolchains",
                         "generator_function": "rules_cc_toolchains",
                         "generator_location": None
                    },
                    "output_tree_hash": "3582bb03a1f513f2b11ce93018ad1fdec4b2d2bc58df9c8dab70b2025a330735"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
          "definition_information": "Repository local_config_sh instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:187:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/sh/sh_configure.bzl:83:14: in sh_configure\nRepository rule sh_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/sh/sh_configure.bzl:72:28: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_sh",
               "generator_name": "local_config_sh",
               "generator_function": "sh_configure",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/sh:sh_configure.bzl%sh_config",
                    "attributes": {
                         "name": "local_config_sh",
                         "generator_name": "local_config_sh",
                         "generator_function": "sh_configure",
                         "generator_location": None
                    },
                    "output_tree_hash": "7bf5ba89669bcdf4526f821bc9f1f9f49409ae9c61c4e8f21c9f17e06c475127"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk11_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:371:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:353:34: in remote_jdk11_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk11_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_11\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"11\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk11_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "244e11245106a8495ac4744a90023b87008e3e553766ba11d47a9fe5b4bb408d"
               }
          ]
     },
     {
          "original_rule_class": "@@build_bazel_apple_support//crosstool:setup.bzl%_apple_cc_autoconf_toolchains",
          "definition_information": "Repository local_config_apple_cc_toolchains instantiated at:\n  /home/brendan/pytorch/WORKSPACE:17:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/lib/repositories.bzl:75:23: in apple_support_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/crosstool/setup.bzl:71:34: in apple_cc_configure\nRepository rule _apple_cc_autoconf_toolchains defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/build_bazel_apple_support/crosstool/setup.bzl:30:48: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_apple_cc_toolchains",
               "generator_name": "local_config_apple_cc_toolchains",
               "generator_function": "apple_support_dependencies",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@build_bazel_apple_support//crosstool:setup.bzl%_apple_cc_autoconf_toolchains",
                    "attributes": {
                         "name": "local_config_apple_cc_toolchains",
                         "generator_name": "local_config_apple_cc_toolchains",
                         "generator_function": "apple_support_dependencies",
                         "generator_location": None
                    },
                    "output_tree_hash": "d5527625a3290689b9dcde30ea50ab1e6188173e312bc3810735c521806720b8"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
               "generator_name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remote_jdk8_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "4d721d8b0731cfb50f963f8b55c7bef9f572de0e2f251f07a12c722ef1acbb2f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "41aa7b3317f8d9001746e908454760bf544ffaa058abe22f40711246608022ba"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "0eb17f6d969bc665a21e55d29eb51e88a067159ee62cf5094b17658a07d3accb"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "c9c795851cffbf2a808bfc7cccea597c3b3fef46cfefa084f7e9de7e90b65447"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "86b129d9c464a9b08f97eca7d8bc5bdb3676b581f8aac044451dbdfaa49e69d3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "fdc8ae00f2436bfc46b2f54c84f2bd84122787ede232a4d61ffc284bfe6f61ec"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_win_toolchain_config_repo",
               "generator_name": "remotejdk17_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_win_toolchain_config_repo",
                         "generator_name": "remotejdk17_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "170c3c9a35e502555dc9f04b345e064880acbf7df935f673154011356f4aad34"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_linux_s390x_toolchain_config_repo",
               "generator_name": "remote_jdk8_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_linux_s390x_toolchain_config_repo",
                         "generator_name": "remote_jdk8_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f1e3f0b4884e21863a7c19a3a12a8995ed4162e02bd07cbb61b42799fc2d7359"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "bb33021f243382d2fb849ec204c5c8be5083c37e081df71d34a84324687cf001"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remote_jdk8_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:370:22: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:349:34: in remote_jdk8_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remote_jdk8_macos_toolchain_config_repo",
               "generator_name": "remote_jdk8_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remote_jdk8_macos_toolchain_config_repo",
                         "generator_name": "remote_jdk8_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_8\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"8\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remote_jdk8_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "e0d82dc2dbe8ec49d859811afe4973ec36226875a39ac7fc8419e91e7e9c89fb"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_win_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_win_toolchain_config_repo",
               "generator_name": "remotejdk21_win_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_win_toolchain_config_repo",
                         "generator_name": "remotejdk21_win_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "87012328b07a779503deec0ef47132a0de50efd69afe7df87619bcc07b1dc4ed"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "ee548ad054c9b75286ff3cd19792e433a2d1236378d3a0d8076fca0bb1a88e05"
               }
          ]
     },
     {
          "original_rule_class": "local_config_platform",
          "original_attributes": {
               "name": "local_config_platform"
          },
          "native": "local_config_platform(name = 'local_config_platform')"
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "f0f07fe0f645f2dc7b8c9953c7962627e1c7425cc52f543729dbff16cd20e461"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "b169b01ac1a169d7eb5e3525454c3e408e9127993ac0f578dc2c5ad183fd4e3e"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "30b78e0951c37c2d7ae1318f83045ff42ef261dbb93c5b4fd3ba963e12cf68d6"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_win_arm64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_win_arm64_toolchain_config_repo",
               "generator_name": "remotejdk21_win_arm64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_win_arm64_toolchain_config_repo",
                         "generator_name": "remotejdk21_win_arm64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:windows\", \"@platforms//cpu:arm64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_win_arm64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "9bbdbb329eeba27bc482582360abc6e3351d9a9a07ee11cba3a0026c90223e85"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_macos_aarch64_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_macos_aarch64_toolchain_config_repo",
               "generator_name": "remotejdk21_macos_aarch64_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_macos_aarch64_toolchain_config_repo",
                         "generator_name": "remotejdk21_macos_aarch64_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:aarch64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos_aarch64//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "706d910cc6809ea7f77fa4f938a4f019dd90d9dad927fb804a14b04321300a36"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_macos_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_macos_toolchain_config_repo",
               "generator_name": "remotejdk21_macos_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_macos_toolchain_config_repo",
                         "generator_name": "remotejdk21_macos_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:macos\", \"@platforms//cpu:x86_64\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_macos//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "434446eddb7f6a3dcc7a2a5330ed9ab26579c5142c19866b197475a695fbb32f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk21_linux_ppc64le_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:373:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:361:34: in remote_jdk21_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
               "generator_name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "generator_name": "remotejdk21_linux_ppc64le_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_21\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"21\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:ppc\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk21_linux_ppc64le//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "7886e497d586c3f3c8225685281b0940e9aa699af208dc98de3db8839e197be3"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
          "definition_information": "Repository remotejdk17_linux_s390x_toolchain_config_repo instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:93:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:372:23: in rules_java_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:357:34: in remote_jdk17_repos\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/java/repositories.bzl:333:14: in _remote_jdk_repos_for_version\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:57:22: in remote_java_repository\nRepository rule _toolchain_config defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/remote_java_repository.bzl:27:36: in <toplevel>\n",
          "original_attributes": {
               "name": "remotejdk17_linux_s390x_toolchain_config_repo",
               "generator_name": "remotejdk17_linux_s390x_toolchain_config_repo",
               "generator_function": "rules_java_dependencies",
               "generator_location": None,
               "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:remote_java_repository.bzl%_toolchain_config",
                    "attributes": {
                         "name": "remotejdk17_linux_s390x_toolchain_config_repo",
                         "generator_name": "remotejdk17_linux_s390x_toolchain_config_repo",
                         "generator_function": "rules_java_dependencies",
                         "generator_location": None,
                         "build_file": "\nconfig_setting(\n    name = \"prefix_version_setting\",\n    values = {\"java_runtime_version\": \"remotejdk_17\"},\n    visibility = [\"//visibility:private\"],\n)\nconfig_setting(\n    name = \"version_setting\",\n    values = {\"java_runtime_version\": \"17\"},\n    visibility = [\"//visibility:private\"],\n)\nalias(\n    name = \"version_or_prefix_version_setting\",\n    actual = select({\n        \":version_setting\": \":version_setting\",\n        \"//conditions:default\": \":prefix_version_setting\",\n    }),\n    visibility = [\"//visibility:private\"],\n)\ntoolchain(\n    name = \"toolchain\",\n    target_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\ntoolchain(\n    name = \"bootstrap_runtime_toolchain\",\n    # These constraints are not required for correctness, but prevent fetches of remote JDK for\n    # different architectures. As every Java compilation toolchain depends on a bootstrap runtime in\n    # the same configuration, this constraint will not result in toolchain resolution failures.\n    exec_compatible_with = [\"@platforms//os:linux\", \"@platforms//cpu:s390x\"],\n    target_settings = [\":version_or_prefix_version_setting\"],\n    toolchain_type = \"@bazel_tools//tools/jdk:bootstrap_runtime_toolchain_type\",\n    toolchain = \"@remotejdk17_linux_s390x//:jdk\",\n)\n"
                    },
                    "output_tree_hash": "6ba1870e09fccfdcd423f4169b966a73f8e9deaff859ec6fb3b626ed61ebd8b5"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_cuda//cuda/private:repositories.bzl%local_cuda",
          "definition_information": "Repository local_cuda instantiated at:\n  /home/brendan/pytorch/WORKSPACE:55:24: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cuda/cuda/private/repositories.bzl:226:15: in rules_cuda_dependencies\nRepository rule local_cuda defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cuda/cuda/private/repositories.bzl:191:29: in <toplevel>\n",
          "original_attributes": {
               "name": "local_cuda",
               "generator_name": "local_cuda",
               "generator_function": "rules_cuda_dependencies",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@rules_cuda//cuda/private:repositories.bzl%local_cuda",
                    "attributes": {
                         "name": "local_cuda",
                         "generator_name": "local_cuda",
                         "generator_function": "rules_cuda_dependencies",
                         "generator_location": None
                    },
                    "output_tree_hash": "ca8f1674e0df1854139d571885f51b1b3d4f584c6e7c6e386740775dcaf99b52"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_java_builtin//toolchains:local_java_repository.bzl%_local_java_repository_rule",
          "definition_information": "Repository local_jdk instantiated at:\n  /DEFAULT.WORKSPACE.SUFFIX:85:6: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/local_java_repository.bzl:335:32: in local_java_repository\nRepository rule _local_java_repository_rule defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_java_builtin/toolchains/local_java_repository.bzl:290:46: in <toplevel>\n",
          "original_attributes": {
               "name": "local_jdk",
               "generator_name": "local_jdk",
               "generator_function": "maybe",
               "generator_location": None,
               "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
               "java_home": "",
               "version": ""
          },
          "repositories": [
               {
                    "rule_class": "@@rules_java_builtin//toolchains:local_java_repository.bzl%_local_java_repository_rule",
                    "attributes": {
                         "name": "local_jdk",
                         "generator_name": "local_jdk",
                         "generator_function": "maybe",
                         "generator_location": None,
                         "build_file_content": "load(\"@rules_java//java:defs.bzl\", \"java_runtime\")\n\npackage(default_visibility = [\"//visibility:public\"])\n\nexports_files([\"WORKSPACE\", \"BUILD.bazel\"])\n\nfilegroup(\n    name = \"jre\",\n    srcs = glob(\n        [\n            \"jre/bin/**\",\n            \"jre/lib/**\",\n        ],\n        allow_empty = True,\n        # In some configurations, Java browser plugin is considered harmful and\n        # common antivirus software blocks access to npjp2.dll interfering with Bazel,\n        # so do not include it in JRE on Windows.\n        exclude = [\"jre/bin/plugin2/**\"],\n    ),\n)\n\nfilegroup(\n    name = \"jdk-bin\",\n    srcs = glob(\n        [\"bin/**\"],\n        # The JDK on Windows sometimes contains a directory called\n        # \"%systemroot%\", which is not a valid label.\n        exclude = [\"**/*%*/**\"],\n    ),\n)\n\n# This folder holds security policies.\nfilegroup(\n    name = \"jdk-conf\",\n    srcs = glob(\n        [\"conf/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-include\",\n    srcs = glob(\n        [\"include/**\"],\n        allow_empty = True,\n    ),\n)\n\nfilegroup(\n    name = \"jdk-lib\",\n    srcs = glob(\n        [\"lib/**\", \"release\"],\n        allow_empty = True,\n        exclude = [\n            \"lib/missioncontrol/**\",\n            \"lib/visualvm/**\",\n        ],\n    ),\n)\n\njava_runtime(\n    name = \"jdk\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jre\",\n    ],\n    # Provide the 'java` binary explicitly so that the correct path is used by\n    # Bazel even when the host platform differs from the execution platform.\n    # Exactly one of the two globs will be empty depending on the host platform.\n    # When --incompatible_disallow_empty_glob is enabled, each individual empty\n    # glob will fail without allow_empty = True, even if the overall result is\n    # non-empty.\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n\nfilegroup(\n    name = \"jdk-jmods\",\n    srcs = glob(\n        [\"jmods/**\"],\n        allow_empty = True,\n    ),\n)\n\njava_runtime(\n    name = \"jdk-with-jmods\",\n    srcs = [\n        \":jdk-bin\",\n        \":jdk-conf\",\n        \":jdk-include\",\n        \":jdk-lib\",\n        \":jdk-jmods\",\n        \":jre\",\n    ],\n    java = glob([\"bin/java.exe\", \"bin/java\"], allow_empty = True)[0],\n    version = {RUNTIME_VERSION},\n)\n",
                         "java_home": "",
                         "version": ""
                    },
                    "output_tree_hash": "8df19dbcb16cecc35a49eeffbaa1d2eacc1f68710ced9586840bdbb07ff3abb2"
               }
          ]
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "cutlass",
               "path": "third_party/cutlass",
               "build_file": "//third_party:cutlass.BUILD"
          },
          "native": "new_local_repository(name = \"cutlass\", path = \"third_party/cutlass\", build_file = Label(\"//third_party:cutlass.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "kineto",
               "path": "third_party/kineto",
               "build_file": "//third_party:kineto.BUILD"
          },
          "native": "new_local_repository(name = \"kineto\", path = \"third_party/kineto\", build_file = Label(\"//third_party:kineto.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "cpp-httplib",
               "path": "third_party/cpp-httplib",
               "build_file": "//third_party:cpp-httplib.BUILD"
          },
          "native": "new_local_repository(name = \"cpp-httplib\", path = \"third_party/cpp-httplib\", build_file = Label(\"//third_party:cpp-httplib.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "tensorpipe",
               "path": "third_party/tensorpipe",
               "build_file": "//third_party:tensorpipe.BUILD"
          },
          "native": "new_local_repository(name = \"tensorpipe\", path = \"third_party/tensorpipe\", build_file = Label(\"//third_party:tensorpipe.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "fbgemm",
               "path": "third_party/fbgemm",
               "build_file": "//third_party:fbgemm/BUILD.bazel"
          },
          "native": "new_local_repository(name = \"fbgemm\", path = \"third_party/fbgemm\", build_file = Label(\"//third_party:fbgemm/BUILD.bazel\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "fmt",
               "path": "third_party/fmt",
               "build_file": "//third_party:fmt.BUILD"
          },
          "native": "new_local_repository(name = \"fmt\", path = \"third_party/fmt\", build_file = Label(\"//third_party:fmt.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "cudnn_frontend",
               "path": "third_party/cudnn_frontend/",
               "build_file": "//third_party:cudnn_frontend.BUILD"
          },
          "native": "new_local_repository(name = \"cudnn_frontend\", path = \"third_party/cudnn_frontend/\", build_file = Label(\"//third_party:cudnn_frontend.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "onnx",
               "path": "third_party/onnx",
               "build_file": "//third_party:onnx.BUILD"
          },
          "native": "new_local_repository(name = \"onnx\", path = \"third_party/onnx\", build_file = Label(\"//third_party:onnx.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "nlohmann",
               "path": "third_party/nlohmann",
               "build_file": "//third_party:nlohmann.BUILD"
          },
          "native": "new_local_repository(name = \"nlohmann\", path = \"third_party/nlohmann\", build_file = Label(\"//third_party:nlohmann.BUILD\"))"
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository rules_proto instantiated at:\n  /home/brendan/pytorch/WORKSPACE:280:14: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/com_google_protobuf/protobuf_deps.bzl:52:21: in protobuf_deps\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "rules_proto",
               "generator_name": "rules_proto",
               "generator_function": "protobuf_deps",
               "generator_location": None,
               "urls": [
                    "https://github.com/bazelbuild/rules_proto/archive/97d8af4dc474595af3900dd85cb3a29ad28cc313.tar.gz"
               ],
               "sha256": "602e7161d9195e50246177e7c55b2f39950a9cf7366f74ed5f22fd45750cd208",
               "strip_prefix": "rules_proto-97d8af4dc474595af3900dd85cb3a29ad28cc313"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/bazelbuild/rules_proto/archive/97d8af4dc474595af3900dd85cb3a29ad28cc313.tar.gz"
                         ],
                         "sha256": "602e7161d9195e50246177e7c55b2f39950a9cf7366f74ed5f22fd45750cd208",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "rules_proto-97d8af4dc474595af3900dd85cb3a29ad28cc313",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "rules_proto"
                    },
                    "output_tree_hash": "4f74a84e9684fc73c48656a9a6c60bdfaed2cabdf5dc7d21da7ae2ee78c7efa3"
               }
          ]
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "cuda",
               "path": "/usr/local/cuda",
               "build_file": "//third_party:cuda.BUILD"
          },
          "native": "new_local_repository(name = \"cuda\", path = \"/usr/local/cuda\", build_file = Label(\"//third_party:cuda.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "ideep",
               "path": "third_party/ideep",
               "build_file": "//third_party:ideep.BUILD"
          },
          "native": "new_local_repository(name = \"ideep\", path = \"third_party/ideep\", build_file = Label(\"//third_party:ideep.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "sleef",
               "path": "third_party/sleef",
               "build_file": "//third_party:sleef.BUILD"
          },
          "native": "new_local_repository(name = \"sleef\", path = \"third_party/sleef\", build_file = Label(\"//third_party:sleef.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "mkl_dnn",
               "path": "third_party/ideep/mkl-dnn",
               "build_file": "//third_party:mkl-dnn.BUILD"
          },
          "native": "new_local_repository(name = \"mkl_dnn\", path = \"third_party/ideep/mkl-dnn\", build_file = Label(\"//third_party:mkl-dnn.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "moodycamel",
               "path": "third_party/concurrentqueue",
               "build_file": "//third_party:moodycamel.BUILD"
          },
          "native": "new_local_repository(name = \"moodycamel\", path = \"third_party/concurrentqueue\", build_file = Label(\"//third_party:moodycamel.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "asmjit",
               "path": "third_party/fbgemm/external/asmjit",
               "build_file": "//third_party:fbgemm/external/asmjit.BUILD"
          },
          "native": "new_local_repository(name = \"asmjit\", path = \"third_party/fbgemm/external/asmjit\", build_file = Label(\"//third_party:fbgemm/external/asmjit.BUILD\"))"
     },
     {
          "original_rule_class": "new_local_repository",
          "original_attributes": {
               "name": "org_pytorch_cpuinfo",
               "path": "third_party/cpuinfo",
               "build_file": "//third_party:cpuinfo/BUILD.bazel"
          },
          "native": "new_local_repository(name = \"org_pytorch_cpuinfo\", path = \"third_party/cpuinfo\", build_file = Label(\"//third_party:cpuinfo/BUILD.bazel\"))"
     },
     {
          "original_rule_class": "@@rules_cc//cc/private/toolchain:cc_configure.bzl%cc_autoconf",
          "definition_information": "Repository local_config_cc instantiated at:\n  /home/brendan/pytorch/WORKSPACE:60:20: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cc/cc/repositories.bzl:10:17: in rules_cc_toolchains\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cc/cc/private/toolchain/cc_configure.bzl:145:16: in cc_configure\nRepository rule cc_autoconf defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_cc/cc/private/toolchain/cc_configure.bzl:108:30: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_cc",
               "generator_name": "local_config_cc",
               "generator_function": "rules_cc_toolchains",
               "generator_location": None
          },
          "repositories": [
               {
                    "rule_class": "@@rules_cc//cc/private/toolchain:cc_configure.bzl%cc_autoconf",
                    "attributes": {
                         "name": "local_config_cc",
                         "generator_name": "local_config_cc",
                         "generator_function": "rules_cc_toolchains",
                         "generator_location": None
                    },
                    "output_tree_hash": "83d6037a7f2b2bd706bdf2d9cc5ab148c9bc7b10c483669bfa4375ca97676c05"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python:repositories.bzl%python_repository",
          "definition_information": "Repository python3_10_x86_64-unknown-linux-gnu instantiated at:\n  /home/brendan/pytorch/WORKSPACE:253:27: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/repositories.bzl:533:26: in python_register_toolchains\nRepository rule python_repository defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/repositories.bzl:366:36: in <toplevel>\n",
          "original_attributes": {
               "name": "python3_10_x86_64-unknown-linux-gnu",
               "generator_name": "python3_10_x86_64-unknown-linux-gnu",
               "generator_function": "python_register_toolchains",
               "generator_location": None,
               "patches": [],
               "platform": "x86_64-unknown-linux-gnu",
               "python_version": "3.10.9",
               "release_filename": "20230116/cpython-3.10.9+20230116-x86_64-unknown-linux-gnu-install_only.tar.gz",
               "sha256": "d196347aeb701a53fe2bb2b095abec38d27d0fa0443f8a1c2023a1bed6e18cdf",
               "strip_prefix": "python",
               "urls": [
                    "https://github.com/indygreg/python-build-standalone/releases/download/20230116/cpython-3.10.9+20230116-x86_64-unknown-linux-gnu-install_only.tar.gz"
               ]
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python:repositories.bzl%python_repository",
                    "attributes": {
                         "coverage_tool": None,
                         "distutils": None,
                         "distutils_content": "",
                         "ignore_root_user_error": False,
                         "name": "python3_10_x86_64-unknown-linux-gnu",
                         "patches": [],
                         "platform": "x86_64-unknown-linux-gnu",
                         "python_version": "3.10.9",
                         "release_filename": "20230116/cpython-3.10.9+20230116-x86_64-unknown-linux-gnu-install_only.tar.gz",
                         "sha256": "d196347aeb701a53fe2bb2b095abec38d27d0fa0443f8a1c2023a1bed6e18cdf",
                         "strip_prefix": "python",
                         "url": [
                              "https://github.com/indygreg/python-build-standalone/releases/download/20230116/cpython-3.10.9+20230116-x86_64-unknown-linux-gnu-install_only.tar.gz"
                         ]
                    },
                    "output_tree_hash": "574ce3e8b718dd074d4633d2949c4a9a8e133d77c6257ab82b09a6afbec88799"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_glog instantiated at:\n  /home/brendan/pytorch/WORKSPACE:81:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_glog",
               "urls": [
                    "https://github.com/google/glog/archive/v0.4.0.tar.gz"
               ],
               "strip_prefix": "glog-0.4.0",
               "build_file_content": "\nlicenses(['notice'])\n\nload(':bazel/glog.bzl', 'glog_library')\n# TODO: figure out why enabling gflags leads to SIGSEV on the logging init\nglog_library(with_gflags=0)\n    "
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/google/glog/archive/v0.4.0.tar.gz"
                         ],
                         "sha256": "",
                         "integrity": "sha256-8oNZrroS8w1z2eRxHvNW3IQohpaBEhYrxzACZFE5w5w=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "glog-0.4.0",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "\nlicenses(['notice'])\n\nload(':bazel/glog.bzl', 'glog_library')\n# TODO: figure out why enabling gflags leads to SIGSEV on the logging init\nglog_library(with_gflags=0)\n    ",
                         "workspace_file_content": "",
                         "name": "com_github_glog"
                    },
                    "output_tree_hash": "8d1bb2271962f7a4d68bd90c986b4fc841206324d86248e4df15e7a49ab6b16a"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository zlib instantiated at:\n  /home/brendan/pytorch/WORKSPACE:280:14: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/com_google_protobuf/protobuf_deps.bzl:19:21: in protobuf_deps\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "zlib",
               "generator_name": "zlib",
               "generator_function": "protobuf_deps",
               "generator_location": None,
               "urls": [
                    "https://github.com/madler/zlib/archive/v1.2.11.tar.gz"
               ],
               "sha256": "629380c90a77b964d896ed37163f5c3a34f6e6d897311f1df2a7016355c45eff",
               "strip_prefix": "zlib-1.2.11",
               "build_file": "@@com_google_protobuf//:third_party/zlib.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/madler/zlib/archive/v1.2.11.tar.gz"
                         ],
                         "sha256": "629380c90a77b964d896ed37163f5c3a34f6e6d897311f1df2a7016355c45eff",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "zlib-1.2.11",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "@@com_google_protobuf//:third_party/zlib.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "zlib"
                    },
                    "output_tree_hash": "7bb7f668ef3dd4c828d19ca4a159af93f4ec630863940ba8f003de2f1e717372"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository com_github_gflags_gflags instantiated at:\n  /home/brendan/pytorch/WORKSPACE:96:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "com_github_gflags_gflags",
               "urls": [
                    "https://github.com/gflags/gflags/archive/v2.2.2.tar.gz"
               ],
               "strip_prefix": "gflags-2.2.2"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://github.com/gflags/gflags/archive/v2.2.2.tar.gz"
                         ],
                         "sha256": "",
                         "integrity": "sha256-NK8vFc9zZ1E7NSvc0kk6sUzkNpLS3NnfxJlJKWbGTc8=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "gflags-2.2.2",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "com_github_gflags_gflags"
                    },
                    "output_tree_hash": "0a9ee35c6109144768bf0e256c4e2c78f06dc8188a7e2501706494701981ad92"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__build instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__build",
               "generator_name": "pypi__build",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/03/97/f58c723ff036a8d8b4d3115377c0a37ed05c1f68dd9a0d66dab5e82c5c1c/build-0.9.0-py3-none-any.whl",
               "sha256": "38a7a2b7a0bdc61a42a0a67509d88c71ecfc37b393baba770fae34e20929ff69",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/03/97/f58c723ff036a8d8b4d3115377c0a37ed05c1f68dd9a0d66dab5e82c5c1c/build-0.9.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "38a7a2b7a0bdc61a42a0a67509d88c71ecfc37b393baba770fae34e20929ff69",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__build"
                    },
                    "output_tree_hash": "ed89e924eda509a3e88e83665b378c377783f1e7f74366fa47436ae8d04076f3"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__click instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__click",
               "generator_name": "pypi__click",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/76/0a/b6c5f311e32aeb3b406e03c079ade51e905ea630fc19d1262a46249c1c86/click-8.0.1-py3-none-any.whl",
               "sha256": "fba402a4a47334742d782209a7c79bc448911afe1149d07bdabdf480b3e2f4b6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/76/0a/b6c5f311e32aeb3b406e03c079ade51e905ea630fc19d1262a46249c1c86/click-8.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "fba402a4a47334742d782209a7c79bc448911afe1149d07bdabdf480b3e2f4b6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__click"
                    },
                    "output_tree_hash": "af29bf4e063f0cdd2f9b4b3cf894a7acd52e4ddebe798407cc6239ac2c77c77d"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__colorama instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__colorama",
               "generator_name": "pypi__colorama",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
               "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__colorama"
                    },
                    "output_tree_hash": "4ba08bfc7514ccc5b37b43a954a8cb32df1a69c2ecc5e62ff039ae4eea9ff438"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__installer instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__installer",
               "generator_name": "pypi__installer",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
               "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/e5/ca/1172b6638d52f2d6caa2dd262ec4c811ba59eee96d54a7701930726bce18/installer-0.7.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "05d1933f0a5ba7d8d6296bb6d5018e7c94fa473ceb10cf198a92ccea19c27b53",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__installer"
                    },
                    "output_tree_hash": "9399a0cb6e37542f53de0da07dacdf07044ab774187f2bef2670a507297ea5ca"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__packaging instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__packaging",
               "generator_name": "pypi__packaging",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/8f/7b/42582927d281d7cb035609cd3a543ffac89b74f3f4ee8e1c50914bcb57eb/packaging-22.0-py3-none-any.whl",
               "sha256": "957e2148ba0e1a3b282772e791ef1d8083648bc131c8ab0c1feba110ce1146c3",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/8f/7b/42582927d281d7cb035609cd3a543ffac89b74f3f4ee8e1c50914bcb57eb/packaging-22.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "957e2148ba0e1a3b282772e791ef1d8083648bc131c8ab0c1feba110ce1146c3",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__packaging"
                    },
                    "output_tree_hash": "3ee37a5d7d1a0b39aa06bdfdf42114efe2976f3018889e1814f89bbbf904cd3c"
               }
          ]
     },
     {
          "original_rule_class": "@@pybind11_bazel//:python_configure.bzl%python_configure",
          "definition_information": "Repository local_config_python instantiated at:\n  /home/brendan/pytorch/WORKSPACE:273:17: in <toplevel>\nRepository rule python_configure defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pybind11_bazel/python_configure.bzl:412:35: in <toplevel>\n",
          "original_attributes": {
               "name": "local_config_python",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3"
          },
          "repositories": [
               {
                    "rule_class": "@@pybind11_bazel//:python_configure.bzl%python_configure",
                    "attributes": {
                         "name": "local_config_python",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3"
                    },
                    "output_tree_hash": "e15507037a6366ff35775cd8aa60d5934e65a56eb2fda8371a09362976556e55"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pep517 instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pep517",
               "generator_name": "pypi__pep517",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",
               "sha256": "4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/ee/2f/ef63e64e9429111e73d3d6cbee80591672d16f2725e648ebc52096f3d323/pep517-0.13.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "4ba4446d80aed5b5eac6509ade100bff3e7943a8489de249654a5ae9b33ee35b",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pep517"
                    },
                    "output_tree_hash": "bca959e394a9c6cc9dfb5a221ef06510bba57c8b62268bb57ae71ac5dbffa0b4"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip",
               "generator_name": "pypi__pip",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/09/bd/2410905c76ee14c62baf69e3f4aa780226c1bbfc9485731ad018e35b0cb5/pip-22.3.1-py3-none-any.whl",
               "sha256": "908c78e6bc29b676ede1c4d57981d490cb892eb45cd8c214ab6298125119e077",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/09/bd/2410905c76ee14c62baf69e3f4aa780226c1bbfc9485731ad018e35b0cb5/pip-22.3.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "908c78e6bc29b676ede1c4d57981d490cb892eb45cd8c214ab6298125119e077",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip"
                    },
                    "output_tree_hash": "6dee17ea095261a6b27834bed3c3db04794a53963f9bd99ee3b84939ccc6278b"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__pip_tools instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__pip_tools",
               "generator_name": "pypi__pip_tools",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/5e/e8/f6d7d1847c7351048da870417724ace5c4506e816b38db02f4d7c675c189/pip_tools-6.12.1-py3-none-any.whl",
               "sha256": "f0c0c0ec57b58250afce458e2e6058b1f30a4263db895b7d72fd6311bf1dc6f7",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/5e/e8/f6d7d1847c7351048da870417724ace5c4506e816b38db02f4d7c675c189/pip_tools-6.12.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "f0c0c0ec57b58250afce458e2e6058b1f30a4263db895b7d72fd6311bf1dc6f7",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__pip_tools"
                    },
                    "output_tree_hash": "1234d02add2d8c80df08689bb34d56908b072ec0793440867fede8c7b82fbb5f"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__setuptools instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__setuptools",
               "generator_name": "pypi__setuptools",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/7c/5b/3d92b9f0f7ca1645cba48c080b54fe7d8b1033a4e5720091d1631c4266db/setuptools-60.10.0-py3-none-any.whl",
               "sha256": "782ef48d58982ddb49920c11a0c5c9c0b02e7d7d1c2ad0aa44e1a1e133051c96",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/7c/5b/3d92b9f0f7ca1645cba48c080b54fe7d8b1033a4e5720091d1631c4266db/setuptools-60.10.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "782ef48d58982ddb49920c11a0c5c9c0b02e7d7d1c2ad0aa44e1a1e133051c96",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__setuptools"
                    },
                    "output_tree_hash": "c007486b351d1f8b67b660c2322686338a2a957bcd8453e14d3f92ee84991489"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__tomli instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__tomli",
               "generator_name": "pypi__tomli",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
               "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl",
                         "urls": [],
                         "sha256": "939de3e7a6161af0c887ef91b7d41a53e7c5a1ca976325f429cb46ea9bc30ecc",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__tomli"
                    },
                    "output_tree_hash": "e61ae9f19fc65260d4807da4e49f00514de0a6758367846350b501ebb2b50d44"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__wheel instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__wheel",
               "generator_name": "pypi__wheel",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/bd/7c/d38a0b30ce22fc26ed7dbc087c6d00851fb3395e9d0dac40bec1f905030c/wheel-0.38.4-py3-none-any.whl",
               "sha256": "b60533f3f5d530e971d6737ca6d58681ee434818fab630c83a734bb10c083ce8",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/bd/7c/d38a0b30ce22fc26ed7dbc087c6d00851fb3395e9d0dac40bec1f905030c/wheel-0.38.4-py3-none-any.whl",
                         "urls": [],
                         "sha256": "b60533f3f5d530e971d6737ca6d58681ee434818fab630c83a734bb10c083ce8",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__wheel"
                    },
                    "output_tree_hash": "70caf732b1a63fd66fe331f1882cb2920fa12be7d86fcadabf03597e04214468"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__importlib_metadata instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__importlib_metadata",
               "generator_name": "pypi__importlib_metadata",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/d7/31/74dcb59a601b95fce3b0334e8fc9db758f78e43075f22aeb3677dfb19f4c/importlib_metadata-1.4.0-py2.py3-none-any.whl",
               "sha256": "bdd9b7c397c273bcc9a11d6629a38487cd07154fa255a467bf704cd2c258e359",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/d7/31/74dcb59a601b95fce3b0334e8fc9db758f78e43075f22aeb3677dfb19f4c/importlib_metadata-1.4.0-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "bdd9b7c397c273bcc9a11d6629a38487cd07154fa255a467bf704cd2c258e359",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__importlib_metadata"
                    },
                    "output_tree_hash": "3d2766b93b4f1c254273b92d7344c3b4fb2147cfd14435d53826ca67562c5d09"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__zipp instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__zipp",
               "generator_name": "pypi__zipp",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/f4/50/cc72c5bcd48f6e98219fc4a88a5227e9e28b81637a99c49feba1d51f4d50/zipp-1.0.0-py2.py3-none-any.whl",
               "sha256": "8dda78f06bd1674bd8720df8a50bb47b6e1233c503a4eed8e7810686bde37656",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/f4/50/cc72c5bcd48f6e98219fc4a88a5227e9e28b81637a99c49feba1d51f4d50/zipp-1.0.0-py2.py3-none-any.whl",
                         "urls": [],
                         "sha256": "8dda78f06bd1674bd8720df8a50bb47b6e1233c503a4eed8e7810686bde37656",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__zipp"
                    },
                    "output_tree_hash": "b436ec904f6e381fa108671200ba294af9de8d5ade5b9b27fa48f2994af1cc85"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository pypi__more_itertools instantiated at:\n  /home/brendan/pytorch/WORKSPACE:261:10: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip.bzl:148:29: in pip_parse\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/repositories.bzl:140:14: in pip_install_dependencies\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/utils.bzl:268:18: in maybe\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "pypi__more_itertools",
               "generator_name": "pypi__more_itertools",
               "generator_function": "pip_parse",
               "generator_location": None,
               "url": "https://files.pythonhosted.org/packages/bd/3f/c4b3dbd315e248f84c388bd4a72b131a29f123ecacc37ffb2b3834546e42/more_itertools-8.13.0-py3-none-any.whl",
               "sha256": "c5122bffc5f104d37c1626b8615b511f3427aa5389b94d61e5ef8236bfbc3ddb",
               "type": "zip",
               "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://files.pythonhosted.org/packages/bd/3f/c4b3dbd315e248f84c388bd4a72b131a29f123ecacc37ffb2b3834546e42/more_itertools-8.13.0-py3-none-any.whl",
                         "urls": [],
                         "sha256": "c5122bffc5f104d37c1626b8615b511f3427aa5389b94d61e5ef8236bfbc3ddb",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "zip",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file_content": "package(default_visibility = [\"//visibility:public\"])\n\nload(\"@rules_python//python:defs.bzl\", \"py_library\")\n\npy_library(\n    name = \"lib\",\n    srcs = glob([\"**/*.py\"]),\n    data = glob([\"**/*\"], exclude=[\n        # These entries include those put into user-installed dependencies by\n        # data_exclude in /python/pip_install/tools/bazel.py\n        # to avoid non-determinism following pip install's behavior.\n        \"**/*.py\",\n        \"**/*.pyc\",\n        \"**/* *\",\n        \"**/*.dist-info/RECORD\",\n        \"BUILD\",\n        \"WORKSPACE\",\n    ]),\n    # This makes this directory a top-level in the python import\n    # search path for anything that depends on this.\n    imports = [\".\"],\n)\n",
                         "workspace_file_content": "",
                         "name": "pypi__more_itertools"
                    },
                    "output_tree_hash": "c9c128adb9c43f952c08e86c61ee8bf20aa166483a248cbe25b40a65f53dcc51"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository eigen instantiated at:\n  /home/brendan/pytorch/WORKSPACE:128:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "eigen",
               "url": "https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.zip",
               "build_file": "//third_party:eigen.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://gitlab.com/libeigen/eigen/-/archive/3.3.7/eigen-3.3.7.zip",
                         "urls": [],
                         "sha256": "",
                         "integrity": "sha256-SBURjAhf8dWiH2IhijsqxiVV6bjXus1Qk4kjmOepLEs=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "//third_party:eigen.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "eigen"
                    },
                    "output_tree_hash": "52b834452d0eacefe8b0ffb138e8dc582dcf8a352690b8f73ceb2241e80d28cc"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_typing_extensions instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_typing_extensions",
               "generator_name": "pip_deps_typing_extensions",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "typing-extensions==4.11.0     --hash=sha256:83f085bd5ca59c80295fc2a82ab5dac679cbe02b9f33f7d83af68e241bea51b0     --hash=sha256:c1f94d72897edaf4ce775bb7558d5b79d8126906a14ea5ed1635921406c0387a",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_typing_extensions",
                         "generator_name": "pip_deps_typing_extensions",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "typing-extensions==4.11.0     --hash=sha256:83f085bd5ca59c80295fc2a82ab5dac679cbe02b9f33f7d83af68e241bea51b0     --hash=sha256:c1f94d72897edaf4ce775bb7558d5b79d8126906a14ea5ed1635921406c0387a",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "15f4e93a7c38ae1e93f6be80f484f5c95da9737c862061787c13b0f78a5c9dea"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_requests instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_requests",
               "generator_name": "pip_deps_requests",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "requests==2.32.2     --hash=sha256:dd951ff5ecf3e3b3aa26b40703ba77495dab41da839ae72ef3c8e5d8e2433289     --hash=sha256:fc06670dd0ed212426dfeb94fc1b983d917c4f9847c863f313c9dfaaffb7c23c",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_requests",
                         "generator_name": "pip_deps_requests",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "requests==2.32.2     --hash=sha256:dd951ff5ecf3e3b3aa26b40703ba77495dab41da839ae72ef3c8e5d8e2433289     --hash=sha256:fc06670dd0ed212426dfeb94fc1b983d917c4f9847c863f313c9dfaaffb7c23c",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "955978cf3c9a3e6690db6bb72f90bd1b7e1cc763d2246a33a62037440624198c"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_pyyaml instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_pyyaml",
               "generator_name": "pip_deps_pyyaml",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "pyyaml==6.0.1     --hash=sha256:04ac92ad1925b2cff1db0cfebffb6ffc43457495c9b3c39d3fcae417d7125dc5     --hash=sha256:062582fca9fabdd2c8b54a3ef1c978d786e0f6b3a1510e0ac93ef59e0ddae2bc     --hash=sha256:0d3304d8c0adc42be59c5f8a4d9e3d7379e6955ad754aa9d6ab7a398b59dd1df     --hash=sha256:1635fd110e8d85d55237ab316b5b011de701ea0f29d07611174a1b42f1444741     --hash=sha256:184c5108a2aca3c5b3d3bf9395d50893a7ab82a38004c8f61c258d4428e80206     --hash=sha256:18aeb1bf9a78867dc38b259769503436b7c72f7a1f1f4c93ff9a17de54319b27     --hash=sha256:1d4c7e777c441b20e32f52bd377e0c409713e8bb1386e1099c2415f26e479595     --hash=sha256:1e2722cc9fbb45d9b87631ac70924c11d3a401b2d7f410cc0e3bbf249f2dca62     --hash=sha256:1fe35611261b29bd1de0070f0b2f47cb6ff71fa6595c077e42bd0c419fa27b98     --hash=sha256:28c119d996beec18c05208a8bd78cbe4007878c6dd15091efb73a30e90539696     --hash=sha256:326c013efe8048858a6d312ddd31d56e468118ad4cdeda36c719bf5bb6192290     --hash=sha256:40df9b996c2b73138957fe23a16a4f0ba614f4c0efce1e9406a184b6d07fa3a9     --hash=sha256:42f8152b8dbc4fe7d96729ec2b99c7097d656dc1213a3229ca5383f973a5ed6d     --hash=sha256:49a183be227561de579b4a36efbb21b3eab9651dd81b1858589f796549873dd6     --hash=sha256:4fb147e7a67ef577a588a0e2c17b6db51dda102c71de36f8549b6816a96e1867     --hash=sha256:50550eb667afee136e9a77d6dc71ae76a44df8b3e51e41b77f6de2932bfe0f47     --hash=sha256:510c9deebc5c0225e8c96813043e62b680ba2f9c50a08d3724c7f28a747d1486     --hash=sha256:5773183b6446b2c99bb77e77595dd486303b4faab2b086e7b17bc6bef28865f6     --hash=sha256:596106435fa6ad000c2991a98fa58eeb8656ef2325d7e158344fb33864ed87e3     --hash=sha256:6965a7bc3cf88e5a1c3bd2e0b5c22f8d677dc88a455344035f03399034eb3007     --hash=sha256:69b023b2b4daa7548bcfbd4aa3da05b3a74b772db9e23b982788168117739938     --hash=sha256:6c22bec3fbe2524cde73d7ada88f6566758a8f7227bfbf93a408a9d86bcc12a0     --hash=sha256:704219a11b772aea0d8ecd7058d0082713c3562b4e271b849ad7dc4a5c90c13c     --hash=sha256:7e07cbde391ba96ab58e532ff4803f79c4129397514e1413a7dc761ccd755735     --hash=sha256:81e0b275a9ecc9c0c0c07b4b90ba548307583c125f54d5b6946cfee6360c733d     --hash=sha256:855fb52b0dc35af121542a76b9a84f8d1cd886ea97c84703eaa6d88e37a2ad28     --hash=sha256:8d4e9c88387b0f5c7d5f281e55304de64cf7f9c0021a3525bd3b1c542da3b0e4     --hash=sha256:9046c58c4395dff28dd494285c82ba00b546adfc7ef001486fbf0324bc174fba     --hash=sha256:9eb6caa9a297fc2c2fb8862bc5370d0303ddba53ba97e71f08023b6cd73d16a8     --hash=sha256:a08c6f0fe150303c1c6b71ebcd7213c2858041a7e01975da3a99aed1e7a378ef     --hash=sha256:a0cd17c15d3bb3fa06978b4e8958dcdc6e0174ccea823003a106c7d4d7899ac5     --hash=sha256:afd7e57eddb1a54f0f1a974bc4391af8bcce0b444685d936840f125cf046d5bd     --hash=sha256:b1275ad35a5d18c62a7220633c913e1b42d44b46ee12554e5fd39c70a243d6a3     --hash=sha256:b786eecbdf8499b9ca1d697215862083bd6d2a99965554781d0d8d1ad31e13a0     --hash=sha256:ba336e390cd8e4d1739f42dfe9bb83a3cc2e80f567d8805e11b46f4a943f5515     --hash=sha256:baa90d3f661d43131ca170712d903e6295d1f7a0f595074f151c0aed377c9b9c     --hash=sha256:bc1bf2925a1ecd43da378f4db9e4f799775d6367bdb94671027b73b393a7c42c     --hash=sha256:bd4af7373a854424dabd882decdc5579653d7868b8fb26dc7d0e99f823aa5924     --hash=sha256:bf07ee2fef7014951eeb99f56f39c9bb4af143d8aa3c21b1677805985307da34     --hash=sha256:bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43     --hash=sha256:c8098ddcc2a85b61647b2590f825f3db38891662cfc2fc776415143f599bb859     --hash=sha256:d2b04aac4d386b172d5b9692e2d2da8de7bfb6c387fa4f801fbf6fb2e6ba4673     --hash=sha256:d483d2cdf104e7c9fa60c544d92981f12ad66a457afae824d146093b8c294c54     --hash=sha256:d858aa552c999bc8a8d57426ed01e40bef403cd8ccdd0fc5f6f04a00414cac2a     --hash=sha256:e7d73685e87afe9f3b36c799222440d6cf362062f78be1013661b00c5c6f678b     --hash=sha256:f003ed9ad21d6a4713f0a9b5a7a0a79e08dd0f221aff4525a2be4c346ee60aab     --hash=sha256:f22ac1c3cac4dbc50079e965eba2c1058622631e526bd9afd45fedd49ba781fa     --hash=sha256:faca3bdcf85b2fc05d06ff3fbc1f83e1391b3e724afa3feba7d13eeab355484c     --hash=sha256:fca0e3a251908a499833aa292323f32437106001d436eca0e6e7833256674585     --hash=sha256:fd1592b3fdf65fff2ad0004b5e363300ef59ced41c2e6b3a99d4089fa8c5435d     --hash=sha256:fd66fc5d0da6d9815ba2cebeb4205f95818ff4b79c3ebe268e75d961704af52f",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_pyyaml",
                         "generator_name": "pip_deps_pyyaml",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "pyyaml==6.0.1     --hash=sha256:04ac92ad1925b2cff1db0cfebffb6ffc43457495c9b3c39d3fcae417d7125dc5     --hash=sha256:062582fca9fabdd2c8b54a3ef1c978d786e0f6b3a1510e0ac93ef59e0ddae2bc     --hash=sha256:0d3304d8c0adc42be59c5f8a4d9e3d7379e6955ad754aa9d6ab7a398b59dd1df     --hash=sha256:1635fd110e8d85d55237ab316b5b011de701ea0f29d07611174a1b42f1444741     --hash=sha256:184c5108a2aca3c5b3d3bf9395d50893a7ab82a38004c8f61c258d4428e80206     --hash=sha256:18aeb1bf9a78867dc38b259769503436b7c72f7a1f1f4c93ff9a17de54319b27     --hash=sha256:1d4c7e777c441b20e32f52bd377e0c409713e8bb1386e1099c2415f26e479595     --hash=sha256:1e2722cc9fbb45d9b87631ac70924c11d3a401b2d7f410cc0e3bbf249f2dca62     --hash=sha256:1fe35611261b29bd1de0070f0b2f47cb6ff71fa6595c077e42bd0c419fa27b98     --hash=sha256:28c119d996beec18c05208a8bd78cbe4007878c6dd15091efb73a30e90539696     --hash=sha256:326c013efe8048858a6d312ddd31d56e468118ad4cdeda36c719bf5bb6192290     --hash=sha256:40df9b996c2b73138957fe23a16a4f0ba614f4c0efce1e9406a184b6d07fa3a9     --hash=sha256:42f8152b8dbc4fe7d96729ec2b99c7097d656dc1213a3229ca5383f973a5ed6d     --hash=sha256:49a183be227561de579b4a36efbb21b3eab9651dd81b1858589f796549873dd6     --hash=sha256:4fb147e7a67ef577a588a0e2c17b6db51dda102c71de36f8549b6816a96e1867     --hash=sha256:50550eb667afee136e9a77d6dc71ae76a44df8b3e51e41b77f6de2932bfe0f47     --hash=sha256:510c9deebc5c0225e8c96813043e62b680ba2f9c50a08d3724c7f28a747d1486     --hash=sha256:5773183b6446b2c99bb77e77595dd486303b4faab2b086e7b17bc6bef28865f6     --hash=sha256:596106435fa6ad000c2991a98fa58eeb8656ef2325d7e158344fb33864ed87e3     --hash=sha256:6965a7bc3cf88e5a1c3bd2e0b5c22f8d677dc88a455344035f03399034eb3007     --hash=sha256:69b023b2b4daa7548bcfbd4aa3da05b3a74b772db9e23b982788168117739938     --hash=sha256:6c22bec3fbe2524cde73d7ada88f6566758a8f7227bfbf93a408a9d86bcc12a0     --hash=sha256:704219a11b772aea0d8ecd7058d0082713c3562b4e271b849ad7dc4a5c90c13c     --hash=sha256:7e07cbde391ba96ab58e532ff4803f79c4129397514e1413a7dc761ccd755735     --hash=sha256:81e0b275a9ecc9c0c0c07b4b90ba548307583c125f54d5b6946cfee6360c733d     --hash=sha256:855fb52b0dc35af121542a76b9a84f8d1cd886ea97c84703eaa6d88e37a2ad28     --hash=sha256:8d4e9c88387b0f5c7d5f281e55304de64cf7f9c0021a3525bd3b1c542da3b0e4     --hash=sha256:9046c58c4395dff28dd494285c82ba00b546adfc7ef001486fbf0324bc174fba     --hash=sha256:9eb6caa9a297fc2c2fb8862bc5370d0303ddba53ba97e71f08023b6cd73d16a8     --hash=sha256:a08c6f0fe150303c1c6b71ebcd7213c2858041a7e01975da3a99aed1e7a378ef     --hash=sha256:a0cd17c15d3bb3fa06978b4e8958dcdc6e0174ccea823003a106c7d4d7899ac5     --hash=sha256:afd7e57eddb1a54f0f1a974bc4391af8bcce0b444685d936840f125cf046d5bd     --hash=sha256:b1275ad35a5d18c62a7220633c913e1b42d44b46ee12554e5fd39c70a243d6a3     --hash=sha256:b786eecbdf8499b9ca1d697215862083bd6d2a99965554781d0d8d1ad31e13a0     --hash=sha256:ba336e390cd8e4d1739f42dfe9bb83a3cc2e80f567d8805e11b46f4a943f5515     --hash=sha256:baa90d3f661d43131ca170712d903e6295d1f7a0f595074f151c0aed377c9b9c     --hash=sha256:bc1bf2925a1ecd43da378f4db9e4f799775d6367bdb94671027b73b393a7c42c     --hash=sha256:bd4af7373a854424dabd882decdc5579653d7868b8fb26dc7d0e99f823aa5924     --hash=sha256:bf07ee2fef7014951eeb99f56f39c9bb4af143d8aa3c21b1677805985307da34     --hash=sha256:bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43     --hash=sha256:c8098ddcc2a85b61647b2590f825f3db38891662cfc2fc776415143f599bb859     --hash=sha256:d2b04aac4d386b172d5b9692e2d2da8de7bfb6c387fa4f801fbf6fb2e6ba4673     --hash=sha256:d483d2cdf104e7c9fa60c544d92981f12ad66a457afae824d146093b8c294c54     --hash=sha256:d858aa552c999bc8a8d57426ed01e40bef403cd8ccdd0fc5f6f04a00414cac2a     --hash=sha256:e7d73685e87afe9f3b36c799222440d6cf362062f78be1013661b00c5c6f678b     --hash=sha256:f003ed9ad21d6a4713f0a9b5a7a0a79e08dd0f221aff4525a2be4c346ee60aab     --hash=sha256:f22ac1c3cac4dbc50079e965eba2c1058622631e526bd9afd45fedd49ba781fa     --hash=sha256:faca3bdcf85b2fc05d06ff3fbc1f83e1391b3e724afa3feba7d13eeab355484c     --hash=sha256:fca0e3a251908a499833aa292323f32437106001d436eca0e6e7833256674585     --hash=sha256:fd1592b3fdf65fff2ad0004b5e363300ef59ced41c2e6b3a99d4089fa8c5435d     --hash=sha256:fd66fc5d0da6d9815ba2cebeb4205f95818ff4b79c3ebe268e75d961704af52f",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "7e649c5b0e7b1d732777534f8d94178a151796331af7b6e56f9a92cd911ceaf2"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_setuptools instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_setuptools",
               "generator_name": "pip_deps_setuptools",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "setuptools==70.3.0     --hash=sha256:f171bab1dfbc86b132997f26a119f6056a57950d058587841a0082e8830f9dc5     --hash=sha256:fe384da74336c398e0d956d1cae0669bc02eed936cdb1d49b57de1990dc11ffc",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_setuptools",
                         "generator_name": "pip_deps_setuptools",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "setuptools==70.3.0     --hash=sha256:f171bab1dfbc86b132997f26a119f6056a57950d058587841a0082e8830f9dc5     --hash=sha256:fe384da74336c398e0d956d1cae0669bc02eed936cdb1d49b57de1990dc11ffc",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "03c661d49752539ce3050aab06bfb53117e29849c1cff78e1295875819fdadc4"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_sympy instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_sympy",
               "generator_name": "pip_deps_sympy",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "sympy==1.12     --hash=sha256:c3588cd4295d0c0f603d0f2ae780587e64e2efeedb3521e46b9bb1d08d184fa5     --hash=sha256:ebf595c8dac3e0fdc4152c51878b498396ec7f30e7a914d6071e674d49420fb8",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_sympy",
                         "generator_name": "pip_deps_sympy",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "sympy==1.12     --hash=sha256:c3588cd4295d0c0f603d0f2ae780587e64e2efeedb3521e46b9bb1d08d184fa5     --hash=sha256:ebf595c8dac3e0fdc4152c51878b498396ec7f30e7a914d6071e674d49420fb8",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "2d8d3024d220c3a0728e737e4a07486c8608aa9694ea39c28084c04e99fdd5f9"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_numpy instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_numpy",
               "generator_name": "pip_deps_numpy",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "numpy==1.26.4     --hash=sha256:03a8c78d01d9781b28a6989f6fa1bb2c4f2d51201cf99d3dd875df6fbd96b23b     --hash=sha256:08beddf13648eb95f8d867350f6a018a4be2e5ad54c8d8caed89ebca558b2818     --hash=sha256:1af303d6b2210eb850fcf03064d364652b7120803a0b872f5211f5234b399f20     --hash=sha256:1dda2e7b4ec9dd512f84935c5f126c8bd8b9f2fc001e9f54af255e8c5f16b0e0     --hash=sha256:2a02aba9ed12e4ac4eb3ea9421c420301a0c6460d9830d74a9df87efa4912010     --hash=sha256:2e4ee3380d6de9c9ec04745830fd9e2eccb3e6cf790d39d7b98ffd19b0dd754a     --hash=sha256:3373d5d70a5fe74a2c1bb6d2cfd9609ecf686d47a2d7b1d37a8f3b6bf6003aea     --hash=sha256:47711010ad8555514b434df65f7d7b076bb8261df1ca9bb78f53d3b2db02e95c     --hash=sha256:4c66707fabe114439db9068ee468c26bbdf909cac0fb58686a42a24de1760c71     --hash=sha256:50193e430acfc1346175fcbdaa28ffec49947a06918b7b92130744e81e640110     --hash=sha256:52b8b60467cd7dd1e9ed082188b4e6bb35aa5cdd01777621a1658910745b90be     --hash=sha256:60dedbb91afcbfdc9bc0b1f3f402804070deed7392c23eb7a7f07fa857868e8a     --hash=sha256:62b8e4b1e28009ef2846b4c7852046736bab361f7aeadeb6a5b89ebec3c7055a     --hash=sha256:666dbfb6ec68962c033a450943ded891bed2d54e6755e35e5835d63f4f6931d5     --hash=sha256:675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed     --hash=sha256:679b0076f67ecc0138fd2ede3a8fd196dddc2ad3254069bcb9faf9a79b1cebcd     --hash=sha256:7349ab0fa0c429c82442a27a9673fc802ffdb7c7775fad780226cb234965e53c     --hash=sha256:7ab55401287bfec946ced39700c053796e7cc0e3acbef09993a9ad2adba6ca6e     --hash=sha256:7e50d0a0cc3189f9cb0aeb3a6a6af18c16f59f004b866cd2be1c14b36134a4a0     --hash=sha256:95a7476c59002f2f6c590b9b7b998306fba6a5aa646b1e22ddfeaf8f78c3a29c     --hash=sha256:96ff0b2ad353d8f990b63294c8986f1ec3cb19d749234014f4e7eb0112ceba5a     --hash=sha256:9fad7dcb1aac3c7f0584a5a8133e3a43eeb2fe127f47e3632d43d677c66c102b     --hash=sha256:9ff0f4f29c51e2803569d7a51c2304de5554655a60c5d776e35b4a41413830d0     --hash=sha256:a354325ee03388678242a4d7ebcd08b5c727033fcff3b2f536aea978e15ee9e6     --hash=sha256:a4abb4f9001ad2858e7ac189089c42178fcce737e4169dc61321660f1a96c7d2     --hash=sha256:ab47dbe5cc8210f55aa58e4805fe224dac469cde56b9f731a4c098b91917159a     --hash=sha256:afedb719a9dcfc7eaf2287b839d8198e06dcd4cb5d276a3df279231138e83d30     --hash=sha256:b3ce300f3644fb06443ee2222c2201dd3a89ea6040541412b8fa189341847218     --hash=sha256:b97fe8060236edf3662adfc2c633f56a08ae30560c56310562cb4f95500022d5     --hash=sha256:bfe25acf8b437eb2a8b2d49d443800a5f18508cd811fea3181723922a8a82b07     --hash=sha256:cd25bcecc4974d09257ffcd1f098ee778f7834c3ad767fe5db785be9a4aa9cb2     --hash=sha256:d209d8969599b27ad20994c8e41936ee0964e6da07478d6c35016bc386b66ad4     --hash=sha256:d5241e0a80d808d70546c697135da2c613f30e28251ff8307eb72ba696945764     --hash=sha256:edd8b5fe47dab091176d21bb6de568acdd906d1887a4584a15a9a96a1dca06ef     --hash=sha256:f870204a840a60da0b12273ef34f7051e98c3b5961b61b0c2c1be6dfd64fbcd3     --hash=sha256:ffa75af20b44f8dba823498024771d5ac50620e6915abac414251bd971b4529f",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_numpy",
                         "generator_name": "pip_deps_numpy",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "numpy==1.26.4     --hash=sha256:03a8c78d01d9781b28a6989f6fa1bb2c4f2d51201cf99d3dd875df6fbd96b23b     --hash=sha256:08beddf13648eb95f8d867350f6a018a4be2e5ad54c8d8caed89ebca558b2818     --hash=sha256:1af303d6b2210eb850fcf03064d364652b7120803a0b872f5211f5234b399f20     --hash=sha256:1dda2e7b4ec9dd512f84935c5f126c8bd8b9f2fc001e9f54af255e8c5f16b0e0     --hash=sha256:2a02aba9ed12e4ac4eb3ea9421c420301a0c6460d9830d74a9df87efa4912010     --hash=sha256:2e4ee3380d6de9c9ec04745830fd9e2eccb3e6cf790d39d7b98ffd19b0dd754a     --hash=sha256:3373d5d70a5fe74a2c1bb6d2cfd9609ecf686d47a2d7b1d37a8f3b6bf6003aea     --hash=sha256:47711010ad8555514b434df65f7d7b076bb8261df1ca9bb78f53d3b2db02e95c     --hash=sha256:4c66707fabe114439db9068ee468c26bbdf909cac0fb58686a42a24de1760c71     --hash=sha256:50193e430acfc1346175fcbdaa28ffec49947a06918b7b92130744e81e640110     --hash=sha256:52b8b60467cd7dd1e9ed082188b4e6bb35aa5cdd01777621a1658910745b90be     --hash=sha256:60dedbb91afcbfdc9bc0b1f3f402804070deed7392c23eb7a7f07fa857868e8a     --hash=sha256:62b8e4b1e28009ef2846b4c7852046736bab361f7aeadeb6a5b89ebec3c7055a     --hash=sha256:666dbfb6ec68962c033a450943ded891bed2d54e6755e35e5835d63f4f6931d5     --hash=sha256:675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed     --hash=sha256:679b0076f67ecc0138fd2ede3a8fd196dddc2ad3254069bcb9faf9a79b1cebcd     --hash=sha256:7349ab0fa0c429c82442a27a9673fc802ffdb7c7775fad780226cb234965e53c     --hash=sha256:7ab55401287bfec946ced39700c053796e7cc0e3acbef09993a9ad2adba6ca6e     --hash=sha256:7e50d0a0cc3189f9cb0aeb3a6a6af18c16f59f004b866cd2be1c14b36134a4a0     --hash=sha256:95a7476c59002f2f6c590b9b7b998306fba6a5aa646b1e22ddfeaf8f78c3a29c     --hash=sha256:96ff0b2ad353d8f990b63294c8986f1ec3cb19d749234014f4e7eb0112ceba5a     --hash=sha256:9fad7dcb1aac3c7f0584a5a8133e3a43eeb2fe127f47e3632d43d677c66c102b     --hash=sha256:9ff0f4f29c51e2803569d7a51c2304de5554655a60c5d776e35b4a41413830d0     --hash=sha256:a354325ee03388678242a4d7ebcd08b5c727033fcff3b2f536aea978e15ee9e6     --hash=sha256:a4abb4f9001ad2858e7ac189089c42178fcce737e4169dc61321660f1a96c7d2     --hash=sha256:ab47dbe5cc8210f55aa58e4805fe224dac469cde56b9f731a4c098b91917159a     --hash=sha256:afedb719a9dcfc7eaf2287b839d8198e06dcd4cb5d276a3df279231138e83d30     --hash=sha256:b3ce300f3644fb06443ee2222c2201dd3a89ea6040541412b8fa189341847218     --hash=sha256:b97fe8060236edf3662adfc2c633f56a08ae30560c56310562cb4f95500022d5     --hash=sha256:bfe25acf8b437eb2a8b2d49d443800a5f18508cd811fea3181723922a8a82b07     --hash=sha256:cd25bcecc4974d09257ffcd1f098ee778f7834c3ad767fe5db785be9a4aa9cb2     --hash=sha256:d209d8969599b27ad20994c8e41936ee0964e6da07478d6c35016bc386b66ad4     --hash=sha256:d5241e0a80d808d70546c697135da2c613f30e28251ff8307eb72ba696945764     --hash=sha256:edd8b5fe47dab091176d21bb6de568acdd906d1887a4584a15a9a96a1dca06ef     --hash=sha256:f870204a840a60da0b12273ef34f7051e98c3b5961b61b0c2c1be6dfd64fbcd3     --hash=sha256:ffa75af20b44f8dba823498024771d5ac50620e6915abac414251bd971b4529f",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "8aaa8d2b5d906865b4749101114d2461bef803fc30ec326ca97b378d6525af61"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_idna instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_idna",
               "generator_name": "pip_deps_idna",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "idna==3.7     --hash=sha256:028ff3aadf0609c1fd278d8ea3089299412a7a8b9bd005dd08b9f8285bcb5cfc     --hash=sha256:82fee1fc78add43492d3a1898bfa6d8a904cc97d8427f683ed8e798d07761aa0",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_idna",
                         "generator_name": "pip_deps_idna",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "idna==3.7     --hash=sha256:028ff3aadf0609c1fd278d8ea3089299412a7a8b9bd005dd08b9f8285bcb5cfc     --hash=sha256:82fee1fc78add43492d3a1898bfa6d8a904cc97d8427f683ed8e798d07761aa0",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "9b0cf6b0f7eec799f8a902e349785be11f45575999ffcaf342cebc73ecbc6526"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_certifi instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_certifi",
               "generator_name": "pip_deps_certifi",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "certifi==2024.7.4     --hash=sha256:5a1e7645bc0ec61a09e26c36f6106dd4cf40c6db3a1fb6352b0244e7fb057c7b     --hash=sha256:c198e21b1289c2ab85ee4e67bb4b4ef3ead0892059901a8d5b622f24a1101e90",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_certifi",
                         "generator_name": "pip_deps_certifi",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "certifi==2024.7.4     --hash=sha256:5a1e7645bc0ec61a09e26c36f6106dd4cf40c6db3a1fb6352b0244e7fb057c7b     --hash=sha256:c198e21b1289c2ab85ee4e67bb4b4ef3ead0892059901a8d5b622f24a1101e90",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "64a5b0fd3ed8f658f88fc8778952fa121869e55e6a2e6291a10ee6125309edb9"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_urllib3 instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_urllib3",
               "generator_name": "pip_deps_urllib3",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "urllib3==2.5.0     --hash=sha256:3fc47733c7e419d4bc3f6b3dc2b4f890bb743906a30d56ba4a5bfa4bbff92760     --hash=sha256:e6b01673c0fa6a13e374b50871808eb3bf7046c4b125b216f6bf1cc604cff0dc",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_urllib3",
                         "generator_name": "pip_deps_urllib3",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "urllib3==2.5.0     --hash=sha256:3fc47733c7e419d4bc3f6b3dc2b4f890bb743906a30d56ba4a5bfa4bbff92760     --hash=sha256:e6b01673c0fa6a13e374b50871808eb3bf7046c4b125b216f6bf1cc604cff0dc",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "c26ef3b4e58e02d03e6458e10b9a871f473cd3515c45741296e513417554a64f"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_charset_normalizer instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_charset_normalizer",
               "generator_name": "pip_deps_charset_normalizer",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "charset-normalizer==3.3.2     --hash=sha256:06435b539f889b1f6f4ac1758871aae42dc3a8c0e24ac9e60c2384973ad73027     --hash=sha256:06a81e93cd441c56a9b65d8e1d043daeb97a3d0856d177d5c90ba85acb3db087     --hash=sha256:0a55554a2fa0d408816b3b5cedf0045f4b8e1a6065aec45849de2d6f3f8e9786     --hash=sha256:0b2b64d2bb6d3fb9112bafa732def486049e63de9618b5843bcdd081d8144cd8     --hash=sha256:10955842570876604d404661fbccbc9c7e684caf432c09c715ec38fbae45ae09     --hash=sha256:122c7fa62b130ed55f8f285bfd56d5f4b4a5b503609d181f9ad85e55c89f4185     --hash=sha256:1ceae2f17a9c33cb48e3263960dc5fc8005351ee19db217e9b1bb15d28c02574     --hash=sha256:1d3193f4a680c64b4b6a9115943538edb896edc190f0b222e73761716519268e     --hash=sha256:1f79682fbe303db92bc2b1136016a38a42e835d932bab5b3b1bfcfbf0640e519     --hash=sha256:2127566c664442652f024c837091890cb1942c30937add288223dc895793f898     --hash=sha256:22afcb9f253dac0696b5a4be4a1c0f8762f8239e21b99680099abd9b2b1b2269     --hash=sha256:25baf083bf6f6b341f4121c2f3c548875ee6f5339300e08be3f2b2ba1721cdd3     --hash=sha256:2e81c7b9c8979ce92ed306c249d46894776a909505d8f5a4ba55b14206e3222f     --hash=sha256:3287761bc4ee9e33561a7e058c72ac0938c4f57fe49a09eae428fd88aafe7bb6     --hash=sha256:34d1c8da1e78d2e001f363791c98a272bb734000fcef47a491c1e3b0505657a8     --hash=sha256:37e55c8e51c236f95b033f6fb391d7d7970ba5fe7ff453dad675e88cf303377a     --hash=sha256:3d47fa203a7bd9c5b6cee4736ee84ca03b8ef23193c0d1ca99b5089f72645c73     --hash=sha256:3e4d1f6587322d2788836a99c69062fbb091331ec940e02d12d179c1d53e25fc     --hash=sha256:42cb296636fcc8b0644486d15c12376cb9fa75443e00fb25de0b8602e64c1714     --hash=sha256:45485e01ff4d3630ec0d9617310448a8702f70e9c01906b0d0118bdf9d124cf2     --hash=sha256:4a78b2b446bd7c934f5dcedc588903fb2f5eec172f3d29e52a9096a43722adfc     --hash=sha256:4ab2fe47fae9e0f9dee8c04187ce5d09f48eabe611be8259444906793ab7cbce     --hash=sha256:4d0d1650369165a14e14e1e47b372cfcb31d6ab44e6e33cb2d4e57265290044d     --hash=sha256:549a3a73da901d5bc3ce8d24e0600d1fa85524c10287f6004fbab87672bf3e1e     --hash=sha256:55086ee1064215781fff39a1af09518bc9255b50d6333f2e4c74ca09fac6a8f6     --hash=sha256:572c3763a264ba47b3cf708a44ce965d98555f618ca42c926a9c1616d8f34269     --hash=sha256:573f6eac48f4769d667c4442081b1794f52919e7edada77495aaed9236d13a96     --hash=sha256:5b4c145409bef602a690e7cfad0a15a55c13320ff7a3ad7ca59c13bb8ba4d45d     --hash=sha256:6463effa3186ea09411d50efc7d85360b38d5f09b870c48e4600f63af490e56a     --hash=sha256:65f6f63034100ead094b8744b3b97965785388f308a64cf8d7c34f2f2e5be0c4     --hash=sha256:663946639d296df6a2bb2aa51b60a2454ca1cb29835324c640dafb5ff2131a77     --hash=sha256:6897af51655e3691ff853668779c7bad41579facacf5fd7253b0133308cf000d     --hash=sha256:68d1f8a9e9e37c1223b656399be5d6b448dea850bed7d0f87a8311f1ff3dabb0     --hash=sha256:6ac7ffc7ad6d040517be39eb591cac5ff87416c2537df6ba3cba3bae290c0fed     --hash=sha256:6b3251890fff30ee142c44144871185dbe13b11bab478a88887a639655be1068     --hash=sha256:6c4caeef8fa63d06bd437cd4bdcf3ffefe6738fb1b25951440d80dc7df8c03ac     --hash=sha256:6ef1d82a3af9d3eecdba2321dc1b3c238245d890843e040e41e470ffa64c3e25     --hash=sha256:753f10e867343b4511128c6ed8c82f7bec3bd026875576dfd88483c5c73b2fd8     --hash=sha256:7cd13a2e3ddeed6913a65e66e94b51d80a041145a026c27e6bb76c31a853c6ab     --hash=sha256:7ed9e526742851e8d5cc9e6cf41427dfc6068d4f5a3bb03659444b4cabf6bc26     --hash=sha256:7f04c839ed0b6b98b1a7501a002144b76c18fb1c1850c8b98d458ac269e26ed2     --hash=sha256:802fe99cca7457642125a8a88a084cef28ff0cf9407060f7b93dca5aa25480db     --hash=sha256:80402cd6ee291dcb72644d6eac93785fe2c8b9cb30893c1af5b8fdd753b9d40f     --hash=sha256:8465322196c8b4d7ab6d1e049e4c5cb460d0394da4a27d23cc242fbf0034b6b5     --hash=sha256:86216b5cee4b06df986d214f664305142d9c76df9b6512be2738aa72a2048f99     --hash=sha256:87d1351268731db79e0f8e745d92493ee2841c974128ef629dc518b937d9194c     --hash=sha256:8bdb58ff7ba23002a4c5808d608e4e6c687175724f54a5dade5fa8c67b604e4d     --hash=sha256:8c622a5fe39a48f78944a87d4fb8a53ee07344641b0562c540d840748571b811     --hash=sha256:8d756e44e94489e49571086ef83b2bb8ce311e730092d2c34ca8f7d925cb20aa     --hash=sha256:8f4a014bc36d3c57402e2977dada34f9c12300af536839dc38c0beab8878f38a     --hash=sha256:9063e24fdb1e498ab71cb7419e24622516c4a04476b17a2dab57e8baa30d6e03     --hash=sha256:90d558489962fd4918143277a773316e56c72da56ec7aa3dc3dbbe20fdfed15b     --hash=sha256:923c0c831b7cfcb071580d3f46c4baf50f174be571576556269530f4bbd79d04     --hash=sha256:95f2a5796329323b8f0512e09dbb7a1860c46a39da62ecb2324f116fa8fdc85c     --hash=sha256:96b02a3dc4381e5494fad39be677abcb5e6634bf7b4fa83a6dd3112607547001     --hash=sha256:9f96df6923e21816da7e0ad3fd47dd8f94b2a5ce594e00677c0013018b813458     --hash=sha256:a10af20b82360ab00827f916a6058451b723b4e65030c5a18577c8b2de5b3389     --hash=sha256:a50aebfa173e157099939b17f18600f72f84eed3049e743b68ad15bd69b6bf99     --hash=sha256:a981a536974bbc7a512cf44ed14938cf01030a99e9b3a06dd59578882f06f985     --hash=sha256:a9a8e9031d613fd2009c182b69c7b2c1ef8239a0efb1df3f7c8da66d5dd3d537     --hash=sha256:ae5f4161f18c61806f411a13b0310bea87f987c7d2ecdbdaad0e94eb2e404238     --hash=sha256:aed38f6e4fb3f5d6bf81bfa990a07806be9d83cf7bacef998ab1a9bd660a581f     --hash=sha256:b01b88d45a6fcb69667cd6d2f7a9aeb4bf53760d7fc536bf679ec94fe9f3ff3d     --hash=sha256:b261ccdec7821281dade748d088bb6e9b69e6d15b30652b74cbbac25e280b796     --hash=sha256:b2b0a0c0517616b6869869f8c581d4eb2dd83a4d79e0ebcb7d373ef9956aeb0a     --hash=sha256:b4a23f61ce87adf89be746c8a8974fe1c823c891d8f86eb218bb957c924bb143     --hash=sha256:bd8f7df7d12c2db9fab40bdd87a7c09b1530128315d047a086fa3ae3435cb3a8     --hash=sha256:beb58fe5cdb101e3a055192ac291b7a21e3b7ef4f67fa1d74e331a7f2124341c     --hash=sha256:c002b4ffc0be611f0d9da932eb0f704fe2602a9a949d1f738e4c34c75b0863d5     --hash=sha256:c083af607d2515612056a31f0a8d9e0fcb5876b7bfc0abad3ecd275bc4ebc2d5     --hash=sha256:c180f51afb394e165eafe4ac2936a14bee3eb10debc9d9e4db8958fe36afe711     --hash=sha256:c235ebd9baae02f1b77bcea61bce332cb4331dc3617d254df3323aa01ab47bd4     --hash=sha256:cd70574b12bb8a4d2aaa0094515df2463cb429d8536cfb6c7ce983246983e5a6     --hash=sha256:d0eccceffcb53201b5bfebb52600a5fb483a20b61da9dbc885f8b103cbe7598c     --hash=sha256:d965bba47ddeec8cd560687584e88cf699fd28f192ceb452d1d7ee807c5597b7     --hash=sha256:db364eca23f876da6f9e16c9da0df51aa4f104a972735574842618b8c6d999d4     --hash=sha256:ddbb2551d7e0102e7252db79ba445cdab71b26640817ab1e3e3648dad515003b     --hash=sha256:deb6be0ac38ece9ba87dea880e438f25ca3eddfac8b002a2ec3d9183a454e8ae     --hash=sha256:e06ed3eb3218bc64786f7db41917d4e686cc4856944f53d5bdf83a6884432e12     --hash=sha256:e27ad930a842b4c5eb8ac0016b0a54f5aebbe679340c26101df33424142c143c     --hash=sha256:e537484df0d8f426ce2afb2d0f8e1c3d0b114b83f8850e5f2fbea0e797bd82ae     --hash=sha256:eb00ed941194665c332bf8e078baf037d6c35d7c4f3102ea2d4f16ca94a26dc8     --hash=sha256:eb6904c354526e758fda7167b33005998fb68c46fbc10e013ca97f21ca5c8887     --hash=sha256:eb8821e09e916165e160797a6c17edda0679379a4be5c716c260e836e122f54b     --hash=sha256:efcb3f6676480691518c177e3b465bcddf57cea040302f9f4e6e191af91174d4     --hash=sha256:f27273b60488abe721a075bcca6d7f3964f9f6f067c8c4c605743023d7d3944f     --hash=sha256:f30c3cb33b24454a82faecaf01b19c18562b1e89558fb6c56de4d9118a032fd5     --hash=sha256:fb69256e180cb6c8a894fee62b3afebae785babc1ee98b81cdf68bbca1987f33     --hash=sha256:fd1abc0d89e30cc4e02e4064dc67fcc51bd941eb395c502aac3ec19fab46b519     --hash=sha256:ff8fa367d09b717b2a17a052544193ad76cd49979c805768879cb63d9ca50561",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_charset_normalizer",
                         "generator_name": "pip_deps_charset_normalizer",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "charset-normalizer==3.3.2     --hash=sha256:06435b539f889b1f6f4ac1758871aae42dc3a8c0e24ac9e60c2384973ad73027     --hash=sha256:06a81e93cd441c56a9b65d8e1d043daeb97a3d0856d177d5c90ba85acb3db087     --hash=sha256:0a55554a2fa0d408816b3b5cedf0045f4b8e1a6065aec45849de2d6f3f8e9786     --hash=sha256:0b2b64d2bb6d3fb9112bafa732def486049e63de9618b5843bcdd081d8144cd8     --hash=sha256:10955842570876604d404661fbccbc9c7e684caf432c09c715ec38fbae45ae09     --hash=sha256:122c7fa62b130ed55f8f285bfd56d5f4b4a5b503609d181f9ad85e55c89f4185     --hash=sha256:1ceae2f17a9c33cb48e3263960dc5fc8005351ee19db217e9b1bb15d28c02574     --hash=sha256:1d3193f4a680c64b4b6a9115943538edb896edc190f0b222e73761716519268e     --hash=sha256:1f79682fbe303db92bc2b1136016a38a42e835d932bab5b3b1bfcfbf0640e519     --hash=sha256:2127566c664442652f024c837091890cb1942c30937add288223dc895793f898     --hash=sha256:22afcb9f253dac0696b5a4be4a1c0f8762f8239e21b99680099abd9b2b1b2269     --hash=sha256:25baf083bf6f6b341f4121c2f3c548875ee6f5339300e08be3f2b2ba1721cdd3     --hash=sha256:2e81c7b9c8979ce92ed306c249d46894776a909505d8f5a4ba55b14206e3222f     --hash=sha256:3287761bc4ee9e33561a7e058c72ac0938c4f57fe49a09eae428fd88aafe7bb6     --hash=sha256:34d1c8da1e78d2e001f363791c98a272bb734000fcef47a491c1e3b0505657a8     --hash=sha256:37e55c8e51c236f95b033f6fb391d7d7970ba5fe7ff453dad675e88cf303377a     --hash=sha256:3d47fa203a7bd9c5b6cee4736ee84ca03b8ef23193c0d1ca99b5089f72645c73     --hash=sha256:3e4d1f6587322d2788836a99c69062fbb091331ec940e02d12d179c1d53e25fc     --hash=sha256:42cb296636fcc8b0644486d15c12376cb9fa75443e00fb25de0b8602e64c1714     --hash=sha256:45485e01ff4d3630ec0d9617310448a8702f70e9c01906b0d0118bdf9d124cf2     --hash=sha256:4a78b2b446bd7c934f5dcedc588903fb2f5eec172f3d29e52a9096a43722adfc     --hash=sha256:4ab2fe47fae9e0f9dee8c04187ce5d09f48eabe611be8259444906793ab7cbce     --hash=sha256:4d0d1650369165a14e14e1e47b372cfcb31d6ab44e6e33cb2d4e57265290044d     --hash=sha256:549a3a73da901d5bc3ce8d24e0600d1fa85524c10287f6004fbab87672bf3e1e     --hash=sha256:55086ee1064215781fff39a1af09518bc9255b50d6333f2e4c74ca09fac6a8f6     --hash=sha256:572c3763a264ba47b3cf708a44ce965d98555f618ca42c926a9c1616d8f34269     --hash=sha256:573f6eac48f4769d667c4442081b1794f52919e7edada77495aaed9236d13a96     --hash=sha256:5b4c145409bef602a690e7cfad0a15a55c13320ff7a3ad7ca59c13bb8ba4d45d     --hash=sha256:6463effa3186ea09411d50efc7d85360b38d5f09b870c48e4600f63af490e56a     --hash=sha256:65f6f63034100ead094b8744b3b97965785388f308a64cf8d7c34f2f2e5be0c4     --hash=sha256:663946639d296df6a2bb2aa51b60a2454ca1cb29835324c640dafb5ff2131a77     --hash=sha256:6897af51655e3691ff853668779c7bad41579facacf5fd7253b0133308cf000d     --hash=sha256:68d1f8a9e9e37c1223b656399be5d6b448dea850bed7d0f87a8311f1ff3dabb0     --hash=sha256:6ac7ffc7ad6d040517be39eb591cac5ff87416c2537df6ba3cba3bae290c0fed     --hash=sha256:6b3251890fff30ee142c44144871185dbe13b11bab478a88887a639655be1068     --hash=sha256:6c4caeef8fa63d06bd437cd4bdcf3ffefe6738fb1b25951440d80dc7df8c03ac     --hash=sha256:6ef1d82a3af9d3eecdba2321dc1b3c238245d890843e040e41e470ffa64c3e25     --hash=sha256:753f10e867343b4511128c6ed8c82f7bec3bd026875576dfd88483c5c73b2fd8     --hash=sha256:7cd13a2e3ddeed6913a65e66e94b51d80a041145a026c27e6bb76c31a853c6ab     --hash=sha256:7ed9e526742851e8d5cc9e6cf41427dfc6068d4f5a3bb03659444b4cabf6bc26     --hash=sha256:7f04c839ed0b6b98b1a7501a002144b76c18fb1c1850c8b98d458ac269e26ed2     --hash=sha256:802fe99cca7457642125a8a88a084cef28ff0cf9407060f7b93dca5aa25480db     --hash=sha256:80402cd6ee291dcb72644d6eac93785fe2c8b9cb30893c1af5b8fdd753b9d40f     --hash=sha256:8465322196c8b4d7ab6d1e049e4c5cb460d0394da4a27d23cc242fbf0034b6b5     --hash=sha256:86216b5cee4b06df986d214f664305142d9c76df9b6512be2738aa72a2048f99     --hash=sha256:87d1351268731db79e0f8e745d92493ee2841c974128ef629dc518b937d9194c     --hash=sha256:8bdb58ff7ba23002a4c5808d608e4e6c687175724f54a5dade5fa8c67b604e4d     --hash=sha256:8c622a5fe39a48f78944a87d4fb8a53ee07344641b0562c540d840748571b811     --hash=sha256:8d756e44e94489e49571086ef83b2bb8ce311e730092d2c34ca8f7d925cb20aa     --hash=sha256:8f4a014bc36d3c57402e2977dada34f9c12300af536839dc38c0beab8878f38a     --hash=sha256:9063e24fdb1e498ab71cb7419e24622516c4a04476b17a2dab57e8baa30d6e03     --hash=sha256:90d558489962fd4918143277a773316e56c72da56ec7aa3dc3dbbe20fdfed15b     --hash=sha256:923c0c831b7cfcb071580d3f46c4baf50f174be571576556269530f4bbd79d04     --hash=sha256:95f2a5796329323b8f0512e09dbb7a1860c46a39da62ecb2324f116fa8fdc85c     --hash=sha256:96b02a3dc4381e5494fad39be677abcb5e6634bf7b4fa83a6dd3112607547001     --hash=sha256:9f96df6923e21816da7e0ad3fd47dd8f94b2a5ce594e00677c0013018b813458     --hash=sha256:a10af20b82360ab00827f916a6058451b723b4e65030c5a18577c8b2de5b3389     --hash=sha256:a50aebfa173e157099939b17f18600f72f84eed3049e743b68ad15bd69b6bf99     --hash=sha256:a981a536974bbc7a512cf44ed14938cf01030a99e9b3a06dd59578882f06f985     --hash=sha256:a9a8e9031d613fd2009c182b69c7b2c1ef8239a0efb1df3f7c8da66d5dd3d537     --hash=sha256:ae5f4161f18c61806f411a13b0310bea87f987c7d2ecdbdaad0e94eb2e404238     --hash=sha256:aed38f6e4fb3f5d6bf81bfa990a07806be9d83cf7bacef998ab1a9bd660a581f     --hash=sha256:b01b88d45a6fcb69667cd6d2f7a9aeb4bf53760d7fc536bf679ec94fe9f3ff3d     --hash=sha256:b261ccdec7821281dade748d088bb6e9b69e6d15b30652b74cbbac25e280b796     --hash=sha256:b2b0a0c0517616b6869869f8c581d4eb2dd83a4d79e0ebcb7d373ef9956aeb0a     --hash=sha256:b4a23f61ce87adf89be746c8a8974fe1c823c891d8f86eb218bb957c924bb143     --hash=sha256:bd8f7df7d12c2db9fab40bdd87a7c09b1530128315d047a086fa3ae3435cb3a8     --hash=sha256:beb58fe5cdb101e3a055192ac291b7a21e3b7ef4f67fa1d74e331a7f2124341c     --hash=sha256:c002b4ffc0be611f0d9da932eb0f704fe2602a9a949d1f738e4c34c75b0863d5     --hash=sha256:c083af607d2515612056a31f0a8d9e0fcb5876b7bfc0abad3ecd275bc4ebc2d5     --hash=sha256:c180f51afb394e165eafe4ac2936a14bee3eb10debc9d9e4db8958fe36afe711     --hash=sha256:c235ebd9baae02f1b77bcea61bce332cb4331dc3617d254df3323aa01ab47bd4     --hash=sha256:cd70574b12bb8a4d2aaa0094515df2463cb429d8536cfb6c7ce983246983e5a6     --hash=sha256:d0eccceffcb53201b5bfebb52600a5fb483a20b61da9dbc885f8b103cbe7598c     --hash=sha256:d965bba47ddeec8cd560687584e88cf699fd28f192ceb452d1d7ee807c5597b7     --hash=sha256:db364eca23f876da6f9e16c9da0df51aa4f104a972735574842618b8c6d999d4     --hash=sha256:ddbb2551d7e0102e7252db79ba445cdab71b26640817ab1e3e3648dad515003b     --hash=sha256:deb6be0ac38ece9ba87dea880e438f25ca3eddfac8b002a2ec3d9183a454e8ae     --hash=sha256:e06ed3eb3218bc64786f7db41917d4e686cc4856944f53d5bdf83a6884432e12     --hash=sha256:e27ad930a842b4c5eb8ac0016b0a54f5aebbe679340c26101df33424142c143c     --hash=sha256:e537484df0d8f426ce2afb2d0f8e1c3d0b114b83f8850e5f2fbea0e797bd82ae     --hash=sha256:eb00ed941194665c332bf8e078baf037d6c35d7c4f3102ea2d4f16ca94a26dc8     --hash=sha256:eb6904c354526e758fda7167b33005998fb68c46fbc10e013ca97f21ca5c8887     --hash=sha256:eb8821e09e916165e160797a6c17edda0679379a4be5c716c260e836e122f54b     --hash=sha256:efcb3f6676480691518c177e3b465bcddf57cea040302f9f4e6e191af91174d4     --hash=sha256:f27273b60488abe721a075bcca6d7f3964f9f6f067c8c4c605743023d7d3944f     --hash=sha256:f30c3cb33b24454a82faecaf01b19c18562b1e89558fb6c56de4d9118a032fd5     --hash=sha256:fb69256e180cb6c8a894fee62b3afebae785babc1ee98b81cdf68bbca1987f33     --hash=sha256:fd1abc0d89e30cc4e02e4064dc67fcc51bd941eb395c502aac3ec19fab46b519     --hash=sha256:ff8fa367d09b717b2a17a052544193ad76cd49979c805768879cb63d9ca50561",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "96755f2a9a3a5b0a3d54cad10c187933d1d89746e72942cb7e4b36b5207fa67d"
               }
          ]
     },
     {
          "original_rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
          "definition_information": "Repository pip_deps_mpmath instantiated at:\n  /home/brendan/pytorch/WORKSPACE:269:13: in <toplevel>\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/pip_deps/requirements.bzl:47:20: in install_deps\nRepository rule whl_library defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/rules_python/python/pip_install/pip_repository.bzl:712:30: in <toplevel>\n",
          "original_attributes": {
               "name": "pip_deps_mpmath",
               "generator_name": "pip_deps_mpmath",
               "generator_function": "install_deps",
               "generator_location": None,
               "repo": "pip_deps",
               "requirement": "mpmath==1.3.0     --hash=sha256:7a28eb2a9774d00c7bc92411c19a89209d5da7c4c9a9e227be8330a23a25b91f     --hash=sha256:a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c",
               "download_only": False,
               "enable_implicit_namespace_pkgs": False,
               "environment": {},
               "extra_pip_args": [],
               "isolated": True,
               "pip_data_exclude": [],
               "python_interpreter": "python3",
               "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
               "quiet": True,
               "repo_prefix": "pip_deps_",
               "timeout": 600
          },
          "repositories": [
               {
                    "rule_class": "@@rules_python//python/pip_install:pip_repository.bzl%whl_library",
                    "attributes": {
                         "name": "pip_deps_mpmath",
                         "generator_name": "pip_deps_mpmath",
                         "generator_function": "install_deps",
                         "generator_location": None,
                         "repo": "pip_deps",
                         "requirement": "mpmath==1.3.0     --hash=sha256:7a28eb2a9774d00c7bc92411c19a89209d5da7c4c9a9e227be8330a23a25b91f     --hash=sha256:a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c",
                         "download_only": False,
                         "enable_implicit_namespace_pkgs": False,
                         "environment": {},
                         "extra_pip_args": [],
                         "isolated": True,
                         "pip_data_exclude": [],
                         "python_interpreter": "python3",
                         "python_interpreter_target": "@@python3_10_x86_64-unknown-linux-gnu//:bin/python3",
                         "quiet": True,
                         "repo_prefix": "pip_deps_",
                         "timeout": 600
                    },
                    "output_tree_hash": "323336a46770a0e79100517e2ec9c3aed1ce6a417d94eaa4de3a49f4bc26ffdd"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository mkl instantiated at:\n  /home/brendan/pytorch/WORKSPACE:219:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "mkl",
               "urls": [
                    "https://anaconda.org/anaconda/mkl/2020.0/download/linux-64/mkl-2020.0-166.tar.bz2"
               ],
               "sha256": "59154b30dd74561e90d547f9a3af26c75b6f4546210888f09c9d4db8f4bf9d4c",
               "strip_prefix": "lib",
               "build_file": "//third_party:mkl.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://anaconda.org/anaconda/mkl/2020.0/download/linux-64/mkl-2020.0-166.tar.bz2"
                         ],
                         "sha256": "59154b30dd74561e90d547f9a3af26c75b6f4546210888f09c9d4db8f4bf9d4c",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "lib",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "//third_party:mkl.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "mkl"
                    },
                    "output_tree_hash": "d0ea54c21baf64a7d7e44f3845ab1b320b0a5c8113c81b42200d060e0773b4c6"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository mkl_headers instantiated at:\n  /home/brendan/pytorch/WORKSPACE:229:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "mkl_headers",
               "urls": [
                    "https://anaconda.org/anaconda/mkl-include/2020.0/download/linux-64/mkl-include-2020.0-166.tar.bz2"
               ],
               "sha256": "2af3494a4bebe5ddccfdc43bacc80fcd78d14c1954b81d2c8e3d73b55527af90",
               "build_file": "//third_party:mkl_headers.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "",
                         "urls": [
                              "https://anaconda.org/anaconda/mkl-include/2020.0/download/linux-64/mkl-include-2020.0-166.tar.bz2"
                         ],
                         "sha256": "2af3494a4bebe5ddccfdc43bacc80fcd78d14c1954b81d2c8e3d73b55527af90",
                         "integrity": "",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "//third_party:mkl_headers.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "mkl_headers"
                    },
                    "output_tree_hash": "cde75836155966501568a02cf9480710b45e607518692ad6d141701f4b62c68d"
               }
          ]
     },
     {
          "original_rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
          "definition_information": "Repository cudnn instantiated at:\n  /home/brendan/pytorch/WORKSPACE:288:13: in <toplevel>\nRepository rule http_archive defined at:\n  /home/brendan/.cache/bazel/_bazel_brendan/89f6f0211654284fabe9802449168206/external/bazel_tools/tools/build_defs/repo/http.bzl:387:31: in <toplevel>\n",
          "original_attributes": {
               "name": "cudnn",
               "url": "https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-9.12.0.46_cuda12-archive.tar.xz",
               "strip_prefix": "cudnn-linux-x86_64-9.12.0.46_cuda12-archive",
               "build_file": "//third_party:cudnn.BUILD"
          },
          "repositories": [
               {
                    "rule_class": "@@bazel_tools//tools/build_defs/repo:http.bzl%http_archive",
                    "attributes": {
                         "url": "https://developer.download.nvidia.com/compute/cudnn/redist/cudnn/linux-x86_64/cudnn-linux-x86_64-9.12.0.46_cuda12-archive.tar.xz",
                         "urls": [],
                         "sha256": "",
                         "integrity": "sha256-IfrRs6ij2wGIaBhLIIK9SSYzrlEBdSQy1lV4K9EIsZ4=",
                         "netrc": "",
                         "auth_patterns": {},
                         "canonical_id": "",
                         "strip_prefix": "cudnn-linux-x86_64-9.12.0.46_cuda12-archive",
                         "add_prefix": "",
                         "type": "",
                         "patches": [],
                         "remote_file_urls": {},
                         "remote_file_integrity": {},
                         "remote_patches": {},
                         "remote_patch_strip": 0,
                         "patch_tool": "",
                         "patch_args": [
                              "-p0"
                         ],
                         "patch_cmds": [],
                         "patch_cmds_win": [],
                         "build_file": "//third_party:cudnn.BUILD",
                         "build_file_content": "",
                         "workspace_file_content": "",
                         "name": "cudnn"
                    },
                    "output_tree_hash": "953f0a24c0b85eb887338429033bee9d90aee196723bcd09ee56cf93bb340ffd"
               }
          ]
     }
]