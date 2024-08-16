#ifndef NL5_DLL_H
#define NL5_DLL_H

// Make the DLL function C-callable if using a C++ compiler.
  #ifdef __cplusplus
  extern "C" {
  #endif // __cplusplus
  #ifdef _MSC_VER
    #ifdef __NL5_DLL__ // Define this 
      #define IMP_EXP __declspec(dllexport)
    #else
      #define IMP_EXP __declspec(dllimport)
    #endif
  #else // Linux
    #define IMP_EXP 
  #endif

//---------------------------------------------------------------------------
//
//  nl5_dll.h
//
//---------------------------------------------------------------------------

IMP_EXP char* NL5_GetError();
IMP_EXP char* NL5_GetInfo();
IMP_EXP int NL5_GetLicense(char* name);

IMP_EXP int NL5_Open(char* name);
IMP_EXP int NL5_Close(int ncir);
IMP_EXP int NL5_Save(int ncir);
IMP_EXP int NL5_SaveAs(int ncir, char* name);

IMP_EXP int NL5_GetValue(int ncir, char* name, double* v);
IMP_EXP int NL5_SetValue(int ncir, char* name, double v);
IMP_EXP int NL5_GetText(int ncir, char* name, char* text, int length);
IMP_EXP int NL5_SetText(int ncir, char* name, char* text);

IMP_EXP int NL5_GetParam(int ncir, char* name);
IMP_EXP int NL5_GetParamValue(int ncir, int npar, double* v);
IMP_EXP int NL5_SetParamValue(int ncir, int npar, double v);
IMP_EXP int NL5_GetParamText(int ncir, int npar, char* text, int length);
IMP_EXP int NL5_SetParamText(int ncir, int npar, char* text);

IMP_EXP int NL5_GetTrace(int ncir, char* name);
IMP_EXP int NL5_AddVTrace(int ncir, char* name);
IMP_EXP int NL5_AddITrace(int ncir, char* name);
IMP_EXP int NL5_AddPTrace(int ncir, char* name);
IMP_EXP int NL5_AddVarTrace(int ncir, char* name);
IMP_EXP int NL5_AddFuncTrace(int ncir, char* text);
IMP_EXP int NL5_AddDataTrace(int ncir, char* text);	// New function 09/15/23 
IMP_EXP int NL5_DeleteTrace(int ncir, int ntrace);

IMP_EXP int NL5_SetTimeout(int ncir, int t);
IMP_EXP int NL5_SetStep(int ncir, double step);
IMP_EXP int NL5_GetSimulationTime(int ncir, double* t);
IMP_EXP int NL5_Start(int ncir);
IMP_EXP int NL5_Simulate(int ncir, double interval);
IMP_EXP int NL5_SimulateInterval(int ncir, double interval);
IMP_EXP int NL5_SimulateStep(int ncir);
IMP_EXP int NL5_SaveIC(int ncir);

IMP_EXP int NL5_GetDataSize(int ncir, int ntrace);
IMP_EXP int NL5_GetDataAt(int ncir, int ntrace, int n, double* t, double* data);
IMP_EXP int NL5_GetLastData(int ncir, int ntrace, double* t, double* data);
IMP_EXP int NL5_GetData(int ncir, int ntrace, double t, double* data);
IMP_EXP int NL5_DeleteOldData(int ncir);
IMP_EXP int NL5_SaveData(int ncir, char* name);
IMP_EXP int NL5_AddData(int ncir, int ntrace, double t, double v);  // New function 09/15/23 
IMP_EXP int NL5_DeleteData(int ncir, int trace);  // New function 09/15/23 

IMP_EXP int NL5_GetInput(int ncir, char* name);
IMP_EXP int NL5_SetInputValue(int ncir, int nin, double v);
IMP_EXP int NL5_SetInputLogicalValue(int ncir, int nin, int i);
IMP_EXP int NL5_GetOutput(int ncir, char* name);
IMP_EXP int NL5_GetOutputValue(int ncir, int nout, double* v);
IMP_EXP int NL5_GetOutputLogicalValue(int ncir, int nout, int* i);

IMP_EXP int NL5_SetAC(int ncir, double from, double to, int points, int scale);  // New function 09/15/23 
IMP_EXP int NL5_SetACSource(int ncir, char* name);  // New function 09/15/23 
IMP_EXP int NL5_CalcAC(int ncir);
IMP_EXP int NL5_GetACTrace(int ncir, char* name);
IMP_EXP int NL5_GetACDataSize(int ncir, int ntrace);
IMP_EXP int NL5_GetACDataAt(int ncir, int ntrace, int n, double* f, double* mag, double* phase);
IMP_EXP int NL5_SaveACData(int ncir, char* name);


  #ifdef __cplusplus
}
  #endif // __cplusplus


#endif  // NL5_DLL_H


