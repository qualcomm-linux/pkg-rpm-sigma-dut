<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# sigma-dut RPM - CentOS Stream 10

This branch contains the CentOS Stream 10 RPM packaging for `sigma-dut`.

## Package

| Field | Value |
|---|---|
| Package | `sigma-dut` |
| Version | `dev` |
| Source commit | `a7859766c2bc60bcbc5d6271617141e6853fea8a` |
| Source | `https://github.com/qualcomm/sigma-dut/archive/a7859766c2bc60bcbc5d6271617141e6853fea8a/sigma-dut-a7859766c2bc60bcbc5d6271617141e6853fea8a.tar.gz` |
| Source checksum | See `sources` |

The package installs:

```text
/usr/sbin/sigma_dut
```

`sigma-dut` has no newer upstream release tag for this packaging target, so this
RPM intentionally builds from the fixed commit above and packages it as a `dev`
snapshot instead of a moving branch.

## Files

```text
sigma-dut.spec
sources
.github/workflows/build-on-pr.yml
.github/workflows/pkg-release.yml
```

Do not commit source tarballs or built RPMs. The workflows resolve the tarball
from the lookaside cache, or from `Source0` on a cache miss, then verify it
against `sources`.

## Build

Local validation can be run with `qcom-rpm-utils`:

```bash
/path/to/qcom-rpm-utils/scripts/build-rpm.sh \
  --tarball /path/to/sigma-dut-a7859766c2bc60bcbc5d6271617141e6853fea8a.tar.gz \
  --spec sigma-dut.spec \
  --output /path/to/output
```

For CI, open a PR against this `c10s` branch. The `build-on-pr` workflow builds
RPM artifacts but does not publish them.

## Release

After the PR is merged, run **Actions -> Release** on the `c10s` branch. The
release workflow publishes the generated RPMs to Artifactory after approval.
