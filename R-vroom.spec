#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-vroom
Version  : 1.6.1
Release  : 15
URL      : https://cran.r-project.org/src/contrib/vroom_1.6.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/vroom_1.6.1.tar.gz
Summary  : Read and Write Rectangular Text Data Quickly
Group    : Development/Tools
License  : MIT
Requires: R-vroom-lib = %{version}-%{release}
Requires: R-vroom-license = %{version}-%{release}
Requires: R-bit64
Requires: R-cli
Requires: R-cpp11
Requires: R-crayon
Requires: R-glue
Requires: R-hms
Requires: R-lifecycle
Requires: R-progress
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyselect
Requires: R-tzdb
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-bit64
BuildRequires : R-cli
BuildRequires : R-cpp11
BuildRequires : R-crayon
BuildRequires : R-glue
BuildRequires : R-hms
BuildRequires : R-lifecycle
BuildRequires : R-progress
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-tzdb
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
'tsv' and 'fwf') quickly. When reading it uses a quick initial
    indexing step, then reads the values lazily , so only the data you
    actually use needs to be read.  The writer formats the data in
    parallel and writes to disk asynchronously from formatting.

%package lib
Summary: lib components for the R-vroom package.
Group: Libraries
Requires: R-vroom-license = %{version}-%{release}

%description lib
lib components for the R-vroom package.


%package license
Summary: license components for the R-vroom package.
Group: Default

%description license
license components for the R-vroom package.


%prep
%setup -q -n vroom
cd %{_builddir}/vroom

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678826386

%install
export SOURCE_DATE_EPOCH=1678826386
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-vroom
cp %{_builddir}/vroom/src/mio/LICENSE %{buildroot}/usr/share/package-licenses/R-vroom/eda6909f9b9d9117d4d800f37af80251ab1edd41 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/vroom/COPYRIGHTS
/usr/lib64/R/library/vroom/DESCRIPTION
/usr/lib64/R/library/vroom/INDEX
/usr/lib64/R/library/vroom/LICENSE
/usr/lib64/R/library/vroom/Meta/Rd.rds
/usr/lib64/R/library/vroom/Meta/features.rds
/usr/lib64/R/library/vroom/Meta/hsearch.rds
/usr/lib64/R/library/vroom/Meta/links.rds
/usr/lib64/R/library/vroom/Meta/nsInfo.rds
/usr/lib64/R/library/vroom/Meta/package.rds
/usr/lib64/R/library/vroom/Meta/vignette.rds
/usr/lib64/R/library/vroom/NAMESPACE
/usr/lib64/R/library/vroom/NEWS.md
/usr/lib64/R/library/vroom/R/sysdata.rdb
/usr/lib64/R/library/vroom/R/sysdata.rdx
/usr/lib64/R/library/vroom/R/vroom
/usr/lib64/R/library/vroom/R/vroom.rdb
/usr/lib64/R/library/vroom/R/vroom.rdx
/usr/lib64/R/library/vroom/WORDLIST
/usr/lib64/R/library/vroom/bench/GNUmakefile
/usr/lib64/R/library/vroom/bench/README.md
/usr/lib64/R/library/vroom/bench/all_character-long.tsv
/usr/lib64/R/library/vroom/bench/all_character-long/data.table-data.table.R
/usr/lib64/R/library/vroom/bench/all_character-long/input.R
/usr/lib64/R/library/vroom/bench/all_character-long/read.delim-base.R
/usr/lib64/R/library/vroom/bench/all_character-long/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/all_character-long/vroom-base.R
/usr/lib64/R/library/vroom/bench/all_character-long/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/all_character-long/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/all_character-wide.tsv
/usr/lib64/R/library/vroom/bench/all_character-wide/data.table-data.table.R
/usr/lib64/R/library/vroom/bench/all_character-wide/input.R
/usr/lib64/R/library/vroom/bench/all_character-wide/read.delim-base.R
/usr/lib64/R/library/vroom/bench/all_character-wide/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/all_character-wide/vroom-base.R
/usr/lib64/R/library/vroom/bench/all_character-wide/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/all_character-wide/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/all_numeric-long.tsv
/usr/lib64/R/library/vroom/bench/all_numeric-long/data.table-data.table.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/input.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/read.delim-base.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/vroom-base.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/vroom_no_altrep-base.R
/usr/lib64/R/library/vroom/bench/all_numeric-long/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide.tsv
/usr/lib64/R/library/vroom/bench/all_numeric-wide/data.table-data.table.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/input.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/read.delim-base.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/vroom-base.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/vroom_no_altrep-base.R
/usr/lib64/R/library/vroom/bench/all_numeric-wide/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/download-data.sh
/usr/lib64/R/library/vroom/bench/fwf.tsv
/usr/lib64/R/library/vroom/bench/fwf/read.delim-base.R
/usr/lib64/R/library/vroom/bench/fwf/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/fwf/vroom-base.R
/usr/lib64/R/library/vroom/bench/fwf/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/fwf/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/run-bench-fwf.R
/usr/lib64/R/library/vroom/bench/run-bench.R
/usr/lib64/R/library/vroom/bench/script.sh
/usr/lib64/R/library/vroom/bench/session_info.R
/usr/lib64/R/library/vroom/bench/session_info.tsv
/usr/lib64/R/library/vroom/bench/summarise-benchmarks.R
/usr/lib64/R/library/vroom/bench/taxi.tsv
/usr/lib64/R/library/vroom/bench/taxi/data.table-data.table.R
/usr/lib64/R/library/vroom/bench/taxi/read.delim-base.R
/usr/lib64/R/library/vroom/bench/taxi/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/taxi/vroom-base.R
/usr/lib64/R/library/vroom/bench/taxi/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/taxi/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/taxi_multiple.tsv
/usr/lib64/R/library/vroom/bench/taxi_multiple/data.table-data.table.R
/usr/lib64/R/library/vroom/bench/taxi_multiple/readr-dplyr.R
/usr/lib64/R/library/vroom/bench/taxi_multiple/vroom-base.R
/usr/lib64/R/library/vroom/bench/taxi_multiple/vroom-dplyr.R
/usr/lib64/R/library/vroom/bench/taxi_multiple/vroom_no_altrep-dplyr.R
/usr/lib64/R/library/vroom/bench/taxi_writing.tsv
/usr/lib64/R/library/vroom/bench/taxi_writing/base-gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/base-multithreaded_gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/base-uncompressed.R
/usr/lib64/R/library/vroom/bench/taxi_writing/base-zstandard.R
/usr/lib64/R/library/vroom/bench/taxi_writing/data.table-gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/data.table-multithreaded_gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/data.table-uncompressed.R
/usr/lib64/R/library/vroom/bench/taxi_writing/readr-gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/readr-multithreaded_gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/readr-uncompressed.R
/usr/lib64/R/library/vroom/bench/taxi_writing/readr-zstandard.R
/usr/lib64/R/library/vroom/bench/taxi_writing/vroom-gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/vroom-multithreaded_gzip.R
/usr/lib64/R/library/vroom/bench/taxi_writing/vroom-uncompressed.R
/usr/lib64/R/library/vroom/bench/taxi_writing/vroom-zstandard.R
/usr/lib64/R/library/vroom/doc/benchmarks.R
/usr/lib64/R/library/vroom/doc/benchmarks.Rmd
/usr/lib64/R/library/vroom/doc/benchmarks.html
/usr/lib64/R/library/vroom/doc/index.html
/usr/lib64/R/library/vroom/doc/vroom.R
/usr/lib64/R/library/vroom/doc/vroom.Rmd
/usr/lib64/R/library/vroom/doc/vroom.html
/usr/lib64/R/library/vroom/extdata/fwf-sample.txt
/usr/lib64/R/library/vroom/extdata/mtcars-4.csv
/usr/lib64/R/library/vroom/extdata/mtcars-6.csv
/usr/lib64/R/library/vroom/extdata/mtcars-8.csv
/usr/lib64/R/library/vroom/extdata/mtcars.csv
/usr/lib64/R/library/vroom/extdata/mtcars.csv.bz2
/usr/lib64/R/library/vroom/extdata/mtcars.csv.gz
/usr/lib64/R/library/vroom/extdata/mtcars.csv.xz
/usr/lib64/R/library/vroom/extdata/mtcars.csv.zip
/usr/lib64/R/library/vroom/help/AnIndex
/usr/lib64/R/library/vroom/help/aliases.rds
/usr/lib64/R/library/vroom/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/vroom/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/vroom/help/figures/logo.png
/usr/lib64/R/library/vroom/help/paths.rds
/usr/lib64/R/library/vroom/help/vroom.rdb
/usr/lib64/R/library/vroom/help/vroom.rdx
/usr/lib64/R/library/vroom/html/00Index.html
/usr/lib64/R/library/vroom/html/R.css
/usr/lib64/R/library/vroom/tests/spelling.R
/usr/lib64/R/library/vroom/tests/testthat.R
/usr/lib64/R/library/vroom/tests/testthat/_snaps/col_types.md
/usr/lib64/R/library/vroom/tests/testthat/_snaps/path.md
/usr/lib64/R/library/vroom/tests/testthat/_snaps/problems.md
/usr/lib64/R/library/vroom/tests/testthat/empty-file
/usr/lib64/R/library/vroom/tests/testthat/enc-iso-8859-1.txt
/usr/lib64/R/library/vroom/tests/testthat/fwf-trailing-crlf.txt
/usr/lib64/R/library/vroom/tests/testthat/fwf-trailing.txt
/usr/lib64/R/library/vroom/tests/testthat/helper.R
/usr/lib64/R/library/vroom/tests/testthat/multi-byte-ascii.txt
/usr/lib64/R/library/vroom/tests/testthat/multi-byte-unicode.txt
/usr/lib64/R/library/vroom/tests/testthat/multi-file/bar
/usr/lib64/R/library/vroom/tests/testthat/multi-file/baz
/usr/lib64/R/library/vroom/tests/testthat/multi-file/foo
/usr/lib64/R/library/vroom/tests/testthat/multi-file/qux
/usr/lib64/R/library/vroom/tests/testthat/raw.csv
/usr/lib64/R/library/vroom/tests/testthat/test-big-int.R
/usr/lib64/R/library/vroom/tests/testthat/test-chr.R
/usr/lib64/R/library/vroom/tests/testthat/test-col_types.R
/usr/lib64/R/library/vroom/tests/testthat/test-connection.R
/usr/lib64/R/library/vroom/tests/testthat/test-datetime.R
/usr/lib64/R/library/vroom/tests/testthat/test-dbl.R
/usr/lib64/R/library/vroom/tests/testthat/test-factor.R
/usr/lib64/R/library/vroom/tests/testthat/test-int.R
/usr/lib64/R/library/vroom/tests/testthat/test-logical.R
/usr/lib64/R/library/vroom/tests/testthat/test-multi-byte.R
/usr/lib64/R/library/vroom/tests/testthat/test-multi-file.R
/usr/lib64/R/library/vroom/tests/testthat/test-num.R
/usr/lib64/R/library/vroom/tests/testthat/test-path.R
/usr/lib64/R/library/vroom/tests/testthat/test-problems.R
/usr/lib64/R/library/vroom/tests/testthat/test-select.R
/usr/lib64/R/library/vroom/tests/testthat/test-vroom.R
/usr/lib64/R/library/vroom/tests/testthat/test-vroom_fwf.R
/usr/lib64/R/library/vroom/tests/testthat/test-vroom_lines.R
/usr/lib64/R/library/vroom/tests/testthat/test-vroom_write.R
/usr/lib64/R/library/vroom/words/adjectives.txt
/usr/lib64/R/library/vroom/words/animals.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/vroom/libs/vroom.so
/usr/lib64/R/library/vroom/libs/vroom.so.avx2
/usr/lib64/R/library/vroom/libs/vroom.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-vroom/eda6909f9b9d9117d4d800f37af80251ab1edd41
