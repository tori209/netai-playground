// SPDX-License-Identifier: Apache-2.0
// Copyright Authors of Hubble

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.31.0
// 	protoc        v4.24.0
// source: tetragon/bpf.proto

package tetragon

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type BpfCmd int32

const (
	// Create a map and return a file descriptor that refers to the
	// map.
	BpfCmd_BPF_MAP_CREATE BpfCmd = 0
	// Look up an element with a given key in the map referred to
	// by the file descriptor map_fd.
	BpfCmd_BPF_MAP_LOOKUP_ELEM BpfCmd = 1
	// Create or update an element (key/value pair) in a specified map.
	BpfCmd_BPF_MAP_UPDATE_ELEM BpfCmd = 2
	// Look up and delete an element by key in a specified map.
	BpfCmd_BPF_MAP_DELETE_ELEM BpfCmd = 3
	// Look up an element by key in a specified map and return the key
	// of the next element. Can be used to iterate over all elements
	// in the map.
	BpfCmd_BPF_MAP_GET_NEXT_KEY BpfCmd = 4
	// Verify and load an eBPF program, returning a new file descriptor
	// associated with the program.
	BpfCmd_BPF_PROG_LOAD BpfCmd = 5
	// Pin an eBPF program or map referred by the specified bpf_fd
	// to the provided pathname on the filesystem.
	BpfCmd_BPF_OBJ_PIN BpfCmd = 6
	// Open a file descriptor for the eBPF object pinned to the
	// specified pathname.
	BpfCmd_BPF_OBJ_GET BpfCmd = 7
	// Attach an eBPF program to a target_fd at the specified
	// attach_type hook.
	BpfCmd_BPF_PROG_ATTACH BpfCmd = 8
	// Detach the eBPF program associated with the target_fd at the
	// hook specified by attach_type.
	BpfCmd_BPF_PROG_DETACH BpfCmd = 9
	// Run the eBPF program associated with the prog_fd a repeat
	// number of times against a provided program context ctx_in and
	// data data_in, and return the modified program context
	// ctx_out, data_out (for example, packet data), result of the
	// execution retval, and duration of the test run.
	BpfCmd_BPF_PROG_TEST_RUN BpfCmd = 10
	// Fetch the next eBPF program currently loaded into the kernel.
	BpfCmd_BPF_PROG_GET_NEXT_ID BpfCmd = 11
	// Fetch the next eBPF map currently loaded into the kernel.
	BpfCmd_BPF_MAP_GET_NEXT_ID BpfCmd = 12
	// Open a file descriptor for the eBPF program corresponding to prog_id.
	BpfCmd_BPF_PROG_GET_FD_BY_ID BpfCmd = 13
	// Open a file descriptor for the eBPF map corresponding to map_id.
	BpfCmd_BPF_MAP_GET_FD_BY_ID BpfCmd = 14
	// Obtain information about the eBPF object corresponding to bpf_fd.
	BpfCmd_BPF_OBJ_GET_INFO_BY_FD BpfCmd = 15
	// Obtain information about eBPF programs associated with the specified
	// attach_type hook.
	BpfCmd_BPF_PROG_QUERY BpfCmd = 16
	// Attach an eBPF program to a tracepoint *name* to access kernel
	// internal arguments of the tracepoint in their raw form.
	BpfCmd_BPF_RAW_TRACEPOINT_OPEN BpfCmd = 17
	// Verify and load BPF Type Format (BTF) metadata into the kernel,
	// returning a new file descriptor associated with the metadata.
	BpfCmd_BPF_BTF_LOAD BpfCmd = 18
	// Open a file descriptor for the BPF Type Format (BTF)
	// corresponding to btf_id.
	BpfCmd_BPF_BTF_GET_FD_BY_ID BpfCmd = 19
	// Obtain information about eBPF programs associated with the target
	// process identified by pid and fd.
	BpfCmd_BPF_TASK_FD_QUERY BpfCmd = 20
	// Look up an element with the given key in the map referred to
	// by the file descriptor fd, and if found, delete the element.
	BpfCmd_BPF_MAP_LOOKUP_AND_DELETE_ELEM BpfCmd = 21
	// Freeze the permissions of the specified map.
	BpfCmd_BPF_MAP_FREEZE BpfCmd = 22
	// Fetch the next BPF Type Format (BTF) object currently loaded into
	// the kernel.
	BpfCmd_BPF_BTF_GET_NEXT_ID BpfCmd = 23
	// Iterate and fetch multiple elements in a map.
	BpfCmd_BPF_MAP_LOOKUP_BATCH BpfCmd = 24
	// Iterate and delete all elements in a map.
	BpfCmd_BPF_MAP_LOOKUP_AND_DELETE_BATCH BpfCmd = 25
	// Update multiple elements in a map by key.
	BpfCmd_BPF_MAP_UPDATE_BATCH BpfCmd = 26
	// Delete multiple elements in a map by key.
	BpfCmd_BPF_MAP_DELETE_BATCH BpfCmd = 27
	// Attach an eBPF program to a target_fd at the specified
	// attach_type hook and return a file descriptor handle for
	// managing the link.
	BpfCmd_BPF_LINK_CREATE BpfCmd = 28
	// Update the eBPF program in the specified link_fd to
	// new_prog_fd.
	BpfCmd_BPF_LINK_UPDATE BpfCmd = 29
	// Open a file descriptor for the eBPF Link corresponding to
	// link_id.
	BpfCmd_BPF_LINK_GET_FD_BY_ID BpfCmd = 30
	// Fetch the next eBPF link currently loaded into the kernel.
	BpfCmd_BPF_LINK_GET_NEXT_ID BpfCmd = 31
	// Enable eBPF runtime statistics gathering.
	BpfCmd_BPF_ENABLE_STATS BpfCmd = 32
	// Create an iterator on top of the specified link_fd (as
	// previously created using BPF_LINK_CREATE) and return a
	// file descriptor that can be used to trigger the iteration.
	BpfCmd_BPF_ITER_CREATE BpfCmd = 33
	// Forcefully detach the specified link_fd from its corresponding
	// attachment point.
	BpfCmd_BPF_LINK_DETACH BpfCmd = 34
	// Bind a map to the lifetime of an eBPF program.
	BpfCmd_BPF_PROG_BIND_MAP BpfCmd = 35
	// Create BPF token with embedded information about what can be
	// passed as an extra parameter to various bpf() syscall commands
	// to grant BPF subsystem functionality to unprivileged processes.
	BpfCmd_BPF_TOKEN_CREATE BpfCmd = 36
)

// Enum value maps for BpfCmd.
var (
	BpfCmd_name = map[int32]string{
		0:  "BPF_MAP_CREATE",
		1:  "BPF_MAP_LOOKUP_ELEM",
		2:  "BPF_MAP_UPDATE_ELEM",
		3:  "BPF_MAP_DELETE_ELEM",
		4:  "BPF_MAP_GET_NEXT_KEY",
		5:  "BPF_PROG_LOAD",
		6:  "BPF_OBJ_PIN",
		7:  "BPF_OBJ_GET",
		8:  "BPF_PROG_ATTACH",
		9:  "BPF_PROG_DETACH",
		10: "BPF_PROG_TEST_RUN",
		11: "BPF_PROG_GET_NEXT_ID",
		12: "BPF_MAP_GET_NEXT_ID",
		13: "BPF_PROG_GET_FD_BY_ID",
		14: "BPF_MAP_GET_FD_BY_ID",
		15: "BPF_OBJ_GET_INFO_BY_FD",
		16: "BPF_PROG_QUERY",
		17: "BPF_RAW_TRACEPOINT_OPEN",
		18: "BPF_BTF_LOAD",
		19: "BPF_BTF_GET_FD_BY_ID",
		20: "BPF_TASK_FD_QUERY",
		21: "BPF_MAP_LOOKUP_AND_DELETE_ELEM",
		22: "BPF_MAP_FREEZE",
		23: "BPF_BTF_GET_NEXT_ID",
		24: "BPF_MAP_LOOKUP_BATCH",
		25: "BPF_MAP_LOOKUP_AND_DELETE_BATCH",
		26: "BPF_MAP_UPDATE_BATCH",
		27: "BPF_MAP_DELETE_BATCH",
		28: "BPF_LINK_CREATE",
		29: "BPF_LINK_UPDATE",
		30: "BPF_LINK_GET_FD_BY_ID",
		31: "BPF_LINK_GET_NEXT_ID",
		32: "BPF_ENABLE_STATS",
		33: "BPF_ITER_CREATE",
		34: "BPF_LINK_DETACH",
		35: "BPF_PROG_BIND_MAP",
		36: "BPF_TOKEN_CREATE",
	}
	BpfCmd_value = map[string]int32{
		"BPF_MAP_CREATE":                  0,
		"BPF_MAP_LOOKUP_ELEM":             1,
		"BPF_MAP_UPDATE_ELEM":             2,
		"BPF_MAP_DELETE_ELEM":             3,
		"BPF_MAP_GET_NEXT_KEY":            4,
		"BPF_PROG_LOAD":                   5,
		"BPF_OBJ_PIN":                     6,
		"BPF_OBJ_GET":                     7,
		"BPF_PROG_ATTACH":                 8,
		"BPF_PROG_DETACH":                 9,
		"BPF_PROG_TEST_RUN":               10,
		"BPF_PROG_GET_NEXT_ID":            11,
		"BPF_MAP_GET_NEXT_ID":             12,
		"BPF_PROG_GET_FD_BY_ID":           13,
		"BPF_MAP_GET_FD_BY_ID":            14,
		"BPF_OBJ_GET_INFO_BY_FD":          15,
		"BPF_PROG_QUERY":                  16,
		"BPF_RAW_TRACEPOINT_OPEN":         17,
		"BPF_BTF_LOAD":                    18,
		"BPF_BTF_GET_FD_BY_ID":            19,
		"BPF_TASK_FD_QUERY":               20,
		"BPF_MAP_LOOKUP_AND_DELETE_ELEM":  21,
		"BPF_MAP_FREEZE":                  22,
		"BPF_BTF_GET_NEXT_ID":             23,
		"BPF_MAP_LOOKUP_BATCH":            24,
		"BPF_MAP_LOOKUP_AND_DELETE_BATCH": 25,
		"BPF_MAP_UPDATE_BATCH":            26,
		"BPF_MAP_DELETE_BATCH":            27,
		"BPF_LINK_CREATE":                 28,
		"BPF_LINK_UPDATE":                 29,
		"BPF_LINK_GET_FD_BY_ID":           30,
		"BPF_LINK_GET_NEXT_ID":            31,
		"BPF_ENABLE_STATS":                32,
		"BPF_ITER_CREATE":                 33,
		"BPF_LINK_DETACH":                 34,
		"BPF_PROG_BIND_MAP":               35,
		"BPF_TOKEN_CREATE":                36,
	}
)

func (x BpfCmd) Enum() *BpfCmd {
	p := new(BpfCmd)
	*p = x
	return p
}

func (x BpfCmd) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (BpfCmd) Descriptor() protoreflect.EnumDescriptor {
	return file_tetragon_bpf_proto_enumTypes[0].Descriptor()
}

func (BpfCmd) Type() protoreflect.EnumType {
	return &file_tetragon_bpf_proto_enumTypes[0]
}

func (x BpfCmd) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use BpfCmd.Descriptor instead.
func (BpfCmd) EnumDescriptor() ([]byte, []int) {
	return file_tetragon_bpf_proto_rawDescGZIP(), []int{0}
}

type BpfProgramType int32

const (
	BpfProgramType_BPF_PROG_TYPE_UNSPEC                  BpfProgramType = 0
	BpfProgramType_BPF_PROG_TYPE_SOCKET_FILTER           BpfProgramType = 1
	BpfProgramType_BPF_PROG_TYPE_KPROBE                  BpfProgramType = 2
	BpfProgramType_BPF_PROG_TYPE_SCHED_CLS               BpfProgramType = 3
	BpfProgramType_BPF_PROG_TYPE_SCHED_ACT               BpfProgramType = 4
	BpfProgramType_BPF_PROG_TYPE_TRACEPOINT              BpfProgramType = 5
	BpfProgramType_BPF_PROG_TYPE_XDP                     BpfProgramType = 6
	BpfProgramType_BPF_PROG_TYPE_PERF_EVENT              BpfProgramType = 7
	BpfProgramType_BPF_PROG_TYPE_CGROUP_SKB              BpfProgramType = 8
	BpfProgramType_BPF_PROG_TYPE_CGROUP_SOCK             BpfProgramType = 9
	BpfProgramType_BPF_PROG_TYPE_LWT_IN                  BpfProgramType = 10
	BpfProgramType_BPF_PROG_TYPE_LWT_OUT                 BpfProgramType = 11
	BpfProgramType_BPF_PROG_TYPE_LWT_XMIT                BpfProgramType = 12
	BpfProgramType_BPF_PROG_TYPE_SOCK_OPS                BpfProgramType = 13
	BpfProgramType_BPF_PROG_TYPE_SK_SKB                  BpfProgramType = 14
	BpfProgramType_BPF_PROG_TYPE_CGROUP_DEVICE           BpfProgramType = 15
	BpfProgramType_BPF_PROG_TYPE_SK_MSG                  BpfProgramType = 16
	BpfProgramType_BPF_PROG_TYPE_RAW_TRACEPOINT          BpfProgramType = 17
	BpfProgramType_BPF_PROG_TYPE_CGROUP_SOCK_ADDR        BpfProgramType = 18
	BpfProgramType_BPF_PROG_TYPE_LWT_SEG6LOCAL           BpfProgramType = 19
	BpfProgramType_BPF_PROG_TYPE_LIRC_MODE2              BpfProgramType = 20
	BpfProgramType_BPF_PROG_TYPE_SK_REUSEPORT            BpfProgramType = 21
	BpfProgramType_BPF_PROG_TYPE_FLOW_DISSECTOR          BpfProgramType = 22
	BpfProgramType_BPF_PROG_TYPE_CGROUP_SYSCTL           BpfProgramType = 23
	BpfProgramType_BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE BpfProgramType = 24
	BpfProgramType_BPF_PROG_TYPE_CGROUP_SOCKOPT          BpfProgramType = 25
	BpfProgramType_BPF_PROG_TYPE_TRACING                 BpfProgramType = 26
	BpfProgramType_BPF_PROG_TYPE_STRUCT_OPS              BpfProgramType = 27
	BpfProgramType_BPF_PROG_TYPE_EXT                     BpfProgramType = 28
	BpfProgramType_BPF_PROG_TYPE_LSM                     BpfProgramType = 29
	BpfProgramType_BPF_PROG_TYPE_SK_LOOKUP               BpfProgramType = 30
	BpfProgramType_BPF_PROG_TYPE_SYSCALL                 BpfProgramType = 31
	BpfProgramType_BPF_PROG_TYPE_NETFILTER               BpfProgramType = 32
)

// Enum value maps for BpfProgramType.
var (
	BpfProgramType_name = map[int32]string{
		0:  "BPF_PROG_TYPE_UNSPEC",
		1:  "BPF_PROG_TYPE_SOCKET_FILTER",
		2:  "BPF_PROG_TYPE_KPROBE",
		3:  "BPF_PROG_TYPE_SCHED_CLS",
		4:  "BPF_PROG_TYPE_SCHED_ACT",
		5:  "BPF_PROG_TYPE_TRACEPOINT",
		6:  "BPF_PROG_TYPE_XDP",
		7:  "BPF_PROG_TYPE_PERF_EVENT",
		8:  "BPF_PROG_TYPE_CGROUP_SKB",
		9:  "BPF_PROG_TYPE_CGROUP_SOCK",
		10: "BPF_PROG_TYPE_LWT_IN",
		11: "BPF_PROG_TYPE_LWT_OUT",
		12: "BPF_PROG_TYPE_LWT_XMIT",
		13: "BPF_PROG_TYPE_SOCK_OPS",
		14: "BPF_PROG_TYPE_SK_SKB",
		15: "BPF_PROG_TYPE_CGROUP_DEVICE",
		16: "BPF_PROG_TYPE_SK_MSG",
		17: "BPF_PROG_TYPE_RAW_TRACEPOINT",
		18: "BPF_PROG_TYPE_CGROUP_SOCK_ADDR",
		19: "BPF_PROG_TYPE_LWT_SEG6LOCAL",
		20: "BPF_PROG_TYPE_LIRC_MODE2",
		21: "BPF_PROG_TYPE_SK_REUSEPORT",
		22: "BPF_PROG_TYPE_FLOW_DISSECTOR",
		23: "BPF_PROG_TYPE_CGROUP_SYSCTL",
		24: "BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE",
		25: "BPF_PROG_TYPE_CGROUP_SOCKOPT",
		26: "BPF_PROG_TYPE_TRACING",
		27: "BPF_PROG_TYPE_STRUCT_OPS",
		28: "BPF_PROG_TYPE_EXT",
		29: "BPF_PROG_TYPE_LSM",
		30: "BPF_PROG_TYPE_SK_LOOKUP",
		31: "BPF_PROG_TYPE_SYSCALL",
		32: "BPF_PROG_TYPE_NETFILTER",
	}
	BpfProgramType_value = map[string]int32{
		"BPF_PROG_TYPE_UNSPEC":                  0,
		"BPF_PROG_TYPE_SOCKET_FILTER":           1,
		"BPF_PROG_TYPE_KPROBE":                  2,
		"BPF_PROG_TYPE_SCHED_CLS":               3,
		"BPF_PROG_TYPE_SCHED_ACT":               4,
		"BPF_PROG_TYPE_TRACEPOINT":              5,
		"BPF_PROG_TYPE_XDP":                     6,
		"BPF_PROG_TYPE_PERF_EVENT":              7,
		"BPF_PROG_TYPE_CGROUP_SKB":              8,
		"BPF_PROG_TYPE_CGROUP_SOCK":             9,
		"BPF_PROG_TYPE_LWT_IN":                  10,
		"BPF_PROG_TYPE_LWT_OUT":                 11,
		"BPF_PROG_TYPE_LWT_XMIT":                12,
		"BPF_PROG_TYPE_SOCK_OPS":                13,
		"BPF_PROG_TYPE_SK_SKB":                  14,
		"BPF_PROG_TYPE_CGROUP_DEVICE":           15,
		"BPF_PROG_TYPE_SK_MSG":                  16,
		"BPF_PROG_TYPE_RAW_TRACEPOINT":          17,
		"BPF_PROG_TYPE_CGROUP_SOCK_ADDR":        18,
		"BPF_PROG_TYPE_LWT_SEG6LOCAL":           19,
		"BPF_PROG_TYPE_LIRC_MODE2":              20,
		"BPF_PROG_TYPE_SK_REUSEPORT":            21,
		"BPF_PROG_TYPE_FLOW_DISSECTOR":          22,
		"BPF_PROG_TYPE_CGROUP_SYSCTL":           23,
		"BPF_PROG_TYPE_RAW_TRACEPOINT_WRITABLE": 24,
		"BPF_PROG_TYPE_CGROUP_SOCKOPT":          25,
		"BPF_PROG_TYPE_TRACING":                 26,
		"BPF_PROG_TYPE_STRUCT_OPS":              27,
		"BPF_PROG_TYPE_EXT":                     28,
		"BPF_PROG_TYPE_LSM":                     29,
		"BPF_PROG_TYPE_SK_LOOKUP":               30,
		"BPF_PROG_TYPE_SYSCALL":                 31,
		"BPF_PROG_TYPE_NETFILTER":               32,
	}
)

func (x BpfProgramType) Enum() *BpfProgramType {
	p := new(BpfProgramType)
	*p = x
	return p
}

func (x BpfProgramType) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (BpfProgramType) Descriptor() protoreflect.EnumDescriptor {
	return file_tetragon_bpf_proto_enumTypes[1].Descriptor()
}

func (BpfProgramType) Type() protoreflect.EnumType {
	return &file_tetragon_bpf_proto_enumTypes[1]
}

func (x BpfProgramType) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use BpfProgramType.Descriptor instead.
func (BpfProgramType) EnumDescriptor() ([]byte, []int) {
	return file_tetragon_bpf_proto_rawDescGZIP(), []int{1}
}

var File_tetragon_bpf_proto protoreflect.FileDescriptor

var file_tetragon_bpf_proto_rawDesc = []byte{
	0x0a, 0x12, 0x74, 0x65, 0x74, 0x72, 0x61, 0x67, 0x6f, 0x6e, 0x2f, 0x62, 0x70, 0x66, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x12, 0x08, 0x74, 0x65, 0x74, 0x72, 0x61, 0x67, 0x6f, 0x6e, 0x2a, 0xff,
	0x06, 0x0a, 0x06, 0x42, 0x70, 0x66, 0x43, 0x6d, 0x64, 0x12, 0x12, 0x0a, 0x0e, 0x42, 0x50, 0x46,
	0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x43, 0x52, 0x45, 0x41, 0x54, 0x45, 0x10, 0x00, 0x12, 0x17, 0x0a,
	0x13, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x4c, 0x4f, 0x4f, 0x4b, 0x55, 0x50, 0x5f,
	0x45, 0x4c, 0x45, 0x4d, 0x10, 0x01, 0x12, 0x17, 0x0a, 0x13, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41,
	0x50, 0x5f, 0x55, 0x50, 0x44, 0x41, 0x54, 0x45, 0x5f, 0x45, 0x4c, 0x45, 0x4d, 0x10, 0x02, 0x12,
	0x17, 0x0a, 0x13, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x44, 0x45, 0x4c, 0x45, 0x54,
	0x45, 0x5f, 0x45, 0x4c, 0x45, 0x4d, 0x10, 0x03, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f,
	0x4d, 0x41, 0x50, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x4e, 0x45, 0x58, 0x54, 0x5f, 0x4b, 0x45, 0x59,
	0x10, 0x04, 0x12, 0x11, 0x0a, 0x0d, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x4c,
	0x4f, 0x41, 0x44, 0x10, 0x05, 0x12, 0x0f, 0x0a, 0x0b, 0x42, 0x50, 0x46, 0x5f, 0x4f, 0x42, 0x4a,
	0x5f, 0x50, 0x49, 0x4e, 0x10, 0x06, 0x12, 0x0f, 0x0a, 0x0b, 0x42, 0x50, 0x46, 0x5f, 0x4f, 0x42,
	0x4a, 0x5f, 0x47, 0x45, 0x54, 0x10, 0x07, 0x12, 0x13, 0x0a, 0x0f, 0x42, 0x50, 0x46, 0x5f, 0x50,
	0x52, 0x4f, 0x47, 0x5f, 0x41, 0x54, 0x54, 0x41, 0x43, 0x48, 0x10, 0x08, 0x12, 0x13, 0x0a, 0x0f,
	0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x44, 0x45, 0x54, 0x41, 0x43, 0x48, 0x10,
	0x09, 0x12, 0x15, 0x0a, 0x11, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x45,
	0x53, 0x54, 0x5f, 0x52, 0x55, 0x4e, 0x10, 0x0a, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f,
	0x50, 0x52, 0x4f, 0x47, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x4e, 0x45, 0x58, 0x54, 0x5f, 0x49, 0x44,
	0x10, 0x0b, 0x12, 0x17, 0x0a, 0x13, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x47, 0x45,
	0x54, 0x5f, 0x4e, 0x45, 0x58, 0x54, 0x5f, 0x49, 0x44, 0x10, 0x0c, 0x12, 0x19, 0x0a, 0x15, 0x42,
	0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x46, 0x44, 0x5f, 0x42,
	0x59, 0x5f, 0x49, 0x44, 0x10, 0x0d, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41,
	0x50, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x46, 0x44, 0x5f, 0x42, 0x59, 0x5f, 0x49, 0x44, 0x10, 0x0e,
	0x12, 0x1a, 0x0a, 0x16, 0x42, 0x50, 0x46, 0x5f, 0x4f, 0x42, 0x4a, 0x5f, 0x47, 0x45, 0x54, 0x5f,
	0x49, 0x4e, 0x46, 0x4f, 0x5f, 0x42, 0x59, 0x5f, 0x46, 0x44, 0x10, 0x0f, 0x12, 0x12, 0x0a, 0x0e,
	0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x51, 0x55, 0x45, 0x52, 0x59, 0x10, 0x10,
	0x12, 0x1b, 0x0a, 0x17, 0x42, 0x50, 0x46, 0x5f, 0x52, 0x41, 0x57, 0x5f, 0x54, 0x52, 0x41, 0x43,
	0x45, 0x50, 0x4f, 0x49, 0x4e, 0x54, 0x5f, 0x4f, 0x50, 0x45, 0x4e, 0x10, 0x11, 0x12, 0x10, 0x0a,
	0x0c, 0x42, 0x50, 0x46, 0x5f, 0x42, 0x54, 0x46, 0x5f, 0x4c, 0x4f, 0x41, 0x44, 0x10, 0x12, 0x12,
	0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x42, 0x54, 0x46, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x46,
	0x44, 0x5f, 0x42, 0x59, 0x5f, 0x49, 0x44, 0x10, 0x13, 0x12, 0x15, 0x0a, 0x11, 0x42, 0x50, 0x46,
	0x5f, 0x54, 0x41, 0x53, 0x4b, 0x5f, 0x46, 0x44, 0x5f, 0x51, 0x55, 0x45, 0x52, 0x59, 0x10, 0x14,
	0x12, 0x22, 0x0a, 0x1e, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x4c, 0x4f, 0x4f, 0x4b,
	0x55, 0x50, 0x5f, 0x41, 0x4e, 0x44, 0x5f, 0x44, 0x45, 0x4c, 0x45, 0x54, 0x45, 0x5f, 0x45, 0x4c,
	0x45, 0x4d, 0x10, 0x15, 0x12, 0x12, 0x0a, 0x0e, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f,
	0x46, 0x52, 0x45, 0x45, 0x5a, 0x45, 0x10, 0x16, 0x12, 0x17, 0x0a, 0x13, 0x42, 0x50, 0x46, 0x5f,
	0x42, 0x54, 0x46, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x4e, 0x45, 0x58, 0x54, 0x5f, 0x49, 0x44, 0x10,
	0x17, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x4c, 0x4f, 0x4f,
	0x4b, 0x55, 0x50, 0x5f, 0x42, 0x41, 0x54, 0x43, 0x48, 0x10, 0x18, 0x12, 0x23, 0x0a, 0x1f, 0x42,
	0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x4c, 0x4f, 0x4f, 0x4b, 0x55, 0x50, 0x5f, 0x41, 0x4e,
	0x44, 0x5f, 0x44, 0x45, 0x4c, 0x45, 0x54, 0x45, 0x5f, 0x42, 0x41, 0x54, 0x43, 0x48, 0x10, 0x19,
	0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x55, 0x50, 0x44, 0x41,
	0x54, 0x45, 0x5f, 0x42, 0x41, 0x54, 0x43, 0x48, 0x10, 0x1a, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50,
	0x46, 0x5f, 0x4d, 0x41, 0x50, 0x5f, 0x44, 0x45, 0x4c, 0x45, 0x54, 0x45, 0x5f, 0x42, 0x41, 0x54,
	0x43, 0x48, 0x10, 0x1b, 0x12, 0x13, 0x0a, 0x0f, 0x42, 0x50, 0x46, 0x5f, 0x4c, 0x49, 0x4e, 0x4b,
	0x5f, 0x43, 0x52, 0x45, 0x41, 0x54, 0x45, 0x10, 0x1c, 0x12, 0x13, 0x0a, 0x0f, 0x42, 0x50, 0x46,
	0x5f, 0x4c, 0x49, 0x4e, 0x4b, 0x5f, 0x55, 0x50, 0x44, 0x41, 0x54, 0x45, 0x10, 0x1d, 0x12, 0x19,
	0x0a, 0x15, 0x42, 0x50, 0x46, 0x5f, 0x4c, 0x49, 0x4e, 0x4b, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x46,
	0x44, 0x5f, 0x42, 0x59, 0x5f, 0x49, 0x44, 0x10, 0x1e, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46,
	0x5f, 0x4c, 0x49, 0x4e, 0x4b, 0x5f, 0x47, 0x45, 0x54, 0x5f, 0x4e, 0x45, 0x58, 0x54, 0x5f, 0x49,
	0x44, 0x10, 0x1f, 0x12, 0x14, 0x0a, 0x10, 0x42, 0x50, 0x46, 0x5f, 0x45, 0x4e, 0x41, 0x42, 0x4c,
	0x45, 0x5f, 0x53, 0x54, 0x41, 0x54, 0x53, 0x10, 0x20, 0x12, 0x13, 0x0a, 0x0f, 0x42, 0x50, 0x46,
	0x5f, 0x49, 0x54, 0x45, 0x52, 0x5f, 0x43, 0x52, 0x45, 0x41, 0x54, 0x45, 0x10, 0x21, 0x12, 0x13,
	0x0a, 0x0f, 0x42, 0x50, 0x46, 0x5f, 0x4c, 0x49, 0x4e, 0x4b, 0x5f, 0x44, 0x45, 0x54, 0x41, 0x43,
	0x48, 0x10, 0x22, 0x12, 0x15, 0x0a, 0x11, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f,
	0x42, 0x49, 0x4e, 0x44, 0x5f, 0x4d, 0x41, 0x50, 0x10, 0x23, 0x12, 0x14, 0x0a, 0x10, 0x42, 0x50,
	0x46, 0x5f, 0x54, 0x4f, 0x4b, 0x45, 0x4e, 0x5f, 0x43, 0x52, 0x45, 0x41, 0x54, 0x45, 0x10, 0x24,
	0x2a, 0xe2, 0x07, 0x0a, 0x0e, 0x42, 0x70, 0x66, 0x50, 0x72, 0x6f, 0x67, 0x72, 0x61, 0x6d, 0x54,
	0x79, 0x70, 0x65, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f,
	0x54, 0x59, 0x50, 0x45, 0x5f, 0x55, 0x4e, 0x53, 0x50, 0x45, 0x43, 0x10, 0x00, 0x12, 0x1f, 0x0a,
	0x1b, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53,
	0x4f, 0x43, 0x4b, 0x45, 0x54, 0x5f, 0x46, 0x49, 0x4c, 0x54, 0x45, 0x52, 0x10, 0x01, 0x12, 0x18,
	0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f,
	0x4b, 0x50, 0x52, 0x4f, 0x42, 0x45, 0x10, 0x02, 0x12, 0x1b, 0x0a, 0x17, 0x42, 0x50, 0x46, 0x5f,
	0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x43, 0x48, 0x45, 0x44, 0x5f,
	0x43, 0x4c, 0x53, 0x10, 0x03, 0x12, 0x1b, 0x0a, 0x17, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f,
	0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x43, 0x48, 0x45, 0x44, 0x5f, 0x41, 0x43, 0x54,
	0x10, 0x04, 0x12, 0x1c, 0x0a, 0x18, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54,
	0x59, 0x50, 0x45, 0x5f, 0x54, 0x52, 0x41, 0x43, 0x45, 0x50, 0x4f, 0x49, 0x4e, 0x54, 0x10, 0x05,
	0x12, 0x15, 0x0a, 0x11, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50,
	0x45, 0x5f, 0x58, 0x44, 0x50, 0x10, 0x06, 0x12, 0x1c, 0x0a, 0x18, 0x42, 0x50, 0x46, 0x5f, 0x50,
	0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x50, 0x45, 0x52, 0x46, 0x5f, 0x45, 0x56,
	0x45, 0x4e, 0x54, 0x10, 0x07, 0x12, 0x1c, 0x0a, 0x18, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f,
	0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x43, 0x47, 0x52, 0x4f, 0x55, 0x50, 0x5f, 0x53, 0x4b,
	0x42, 0x10, 0x08, 0x12, 0x1d, 0x0a, 0x19, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f,
	0x54, 0x59, 0x50, 0x45, 0x5f, 0x43, 0x47, 0x52, 0x4f, 0x55, 0x50, 0x5f, 0x53, 0x4f, 0x43, 0x4b,
	0x10, 0x09, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54,
	0x59, 0x50, 0x45, 0x5f, 0x4c, 0x57, 0x54, 0x5f, 0x49, 0x4e, 0x10, 0x0a, 0x12, 0x19, 0x0a, 0x15,
	0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4c, 0x57,
	0x54, 0x5f, 0x4f, 0x55, 0x54, 0x10, 0x0b, 0x12, 0x1a, 0x0a, 0x16, 0x42, 0x50, 0x46, 0x5f, 0x50,
	0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4c, 0x57, 0x54, 0x5f, 0x58, 0x4d, 0x49,
	0x54, 0x10, 0x0c, 0x12, 0x1a, 0x0a, 0x16, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f,
	0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x4f, 0x43, 0x4b, 0x5f, 0x4f, 0x50, 0x53, 0x10, 0x0d, 0x12,
	0x18, 0x0a, 0x14, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45,
	0x5f, 0x53, 0x4b, 0x5f, 0x53, 0x4b, 0x42, 0x10, 0x0e, 0x12, 0x1f, 0x0a, 0x1b, 0x42, 0x50, 0x46,
	0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x43, 0x47, 0x52, 0x4f, 0x55,
	0x50, 0x5f, 0x44, 0x45, 0x56, 0x49, 0x43, 0x45, 0x10, 0x0f, 0x12, 0x18, 0x0a, 0x14, 0x42, 0x50,
	0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x4b, 0x5f, 0x4d,
	0x53, 0x47, 0x10, 0x10, 0x12, 0x20, 0x0a, 0x1c, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47,
	0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x52, 0x41, 0x57, 0x5f, 0x54, 0x52, 0x41, 0x43, 0x45, 0x50,
	0x4f, 0x49, 0x4e, 0x54, 0x10, 0x11, 0x12, 0x22, 0x0a, 0x1e, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52,
	0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x43, 0x47, 0x52, 0x4f, 0x55, 0x50, 0x5f, 0x53,
	0x4f, 0x43, 0x4b, 0x5f, 0x41, 0x44, 0x44, 0x52, 0x10, 0x12, 0x12, 0x1f, 0x0a, 0x1b, 0x42, 0x50,
	0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4c, 0x57, 0x54, 0x5f,
	0x53, 0x45, 0x47, 0x36, 0x4c, 0x4f, 0x43, 0x41, 0x4c, 0x10, 0x13, 0x12, 0x1c, 0x0a, 0x18, 0x42,
	0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4c, 0x49, 0x52,
	0x43, 0x5f, 0x4d, 0x4f, 0x44, 0x45, 0x32, 0x10, 0x14, 0x12, 0x1e, 0x0a, 0x1a, 0x42, 0x50, 0x46,
	0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x4b, 0x5f, 0x52, 0x45,
	0x55, 0x53, 0x45, 0x50, 0x4f, 0x52, 0x54, 0x10, 0x15, 0x12, 0x20, 0x0a, 0x1c, 0x42, 0x50, 0x46,
	0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x46, 0x4c, 0x4f, 0x57, 0x5f,
	0x44, 0x49, 0x53, 0x53, 0x45, 0x43, 0x54, 0x4f, 0x52, 0x10, 0x16, 0x12, 0x1f, 0x0a, 0x1b, 0x42,
	0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x43, 0x47, 0x52,
	0x4f, 0x55, 0x50, 0x5f, 0x53, 0x59, 0x53, 0x43, 0x54, 0x4c, 0x10, 0x17, 0x12, 0x29, 0x0a, 0x25,
	0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x52, 0x41,
	0x57, 0x5f, 0x54, 0x52, 0x41, 0x43, 0x45, 0x50, 0x4f, 0x49, 0x4e, 0x54, 0x5f, 0x57, 0x52, 0x49,
	0x54, 0x41, 0x42, 0x4c, 0x45, 0x10, 0x18, 0x12, 0x20, 0x0a, 0x1c, 0x42, 0x50, 0x46, 0x5f, 0x50,
	0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x43, 0x47, 0x52, 0x4f, 0x55, 0x50, 0x5f,
	0x53, 0x4f, 0x43, 0x4b, 0x4f, 0x50, 0x54, 0x10, 0x19, 0x12, 0x19, 0x0a, 0x15, 0x42, 0x50, 0x46,
	0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x54, 0x52, 0x41, 0x43, 0x49,
	0x4e, 0x47, 0x10, 0x1a, 0x12, 0x1c, 0x0a, 0x18, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47,
	0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x54, 0x52, 0x55, 0x43, 0x54, 0x5f, 0x4f, 0x50, 0x53,
	0x10, 0x1b, 0x12, 0x15, 0x0a, 0x11, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54,
	0x59, 0x50, 0x45, 0x5f, 0x45, 0x58, 0x54, 0x10, 0x1c, 0x12, 0x15, 0x0a, 0x11, 0x42, 0x50, 0x46,
	0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4c, 0x53, 0x4d, 0x10, 0x1d,
	0x12, 0x1b, 0x0a, 0x17, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50,
	0x45, 0x5f, 0x53, 0x4b, 0x5f, 0x4c, 0x4f, 0x4f, 0x4b, 0x55, 0x50, 0x10, 0x1e, 0x12, 0x19, 0x0a,
	0x15, 0x42, 0x50, 0x46, 0x5f, 0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53,
	0x59, 0x53, 0x43, 0x41, 0x4c, 0x4c, 0x10, 0x1f, 0x12, 0x1b, 0x0a, 0x17, 0x42, 0x50, 0x46, 0x5f,
	0x50, 0x52, 0x4f, 0x47, 0x5f, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4e, 0x45, 0x54, 0x46, 0x49, 0x4c,
	0x54, 0x45, 0x52, 0x10, 0x20, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_tetragon_bpf_proto_rawDescOnce sync.Once
	file_tetragon_bpf_proto_rawDescData = file_tetragon_bpf_proto_rawDesc
)

func file_tetragon_bpf_proto_rawDescGZIP() []byte {
	file_tetragon_bpf_proto_rawDescOnce.Do(func() {
		file_tetragon_bpf_proto_rawDescData = protoimpl.X.CompressGZIP(file_tetragon_bpf_proto_rawDescData)
	})
	return file_tetragon_bpf_proto_rawDescData
}

var file_tetragon_bpf_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_tetragon_bpf_proto_goTypes = []interface{}{
	(BpfCmd)(0),         // 0: tetragon.BpfCmd
	(BpfProgramType)(0), // 1: tetragon.BpfProgramType
}
var file_tetragon_bpf_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_tetragon_bpf_proto_init() }
func file_tetragon_bpf_proto_init() {
	if File_tetragon_bpf_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_tetragon_bpf_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_tetragon_bpf_proto_goTypes,
		DependencyIndexes: file_tetragon_bpf_proto_depIdxs,
		EnumInfos:         file_tetragon_bpf_proto_enumTypes,
	}.Build()
	File_tetragon_bpf_proto = out.File
	file_tetragon_bpf_proto_rawDesc = nil
	file_tetragon_bpf_proto_goTypes = nil
	file_tetragon_bpf_proto_depIdxs = nil
}
