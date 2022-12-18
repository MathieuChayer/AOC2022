@echo off

for /L %%i in (1,1,25) do (
  md "DAY %%i"
  cd "DAY %%i"
  type nul > "day%%i_demo.txt"
  type nul > "day%%i.py"
  cd ..
)
