%module libsequence

%include ../../libsequence.i

%inline %{
using namespace std;
template<typename T>  T Dereference( T x[], int i ){
    return x[i];
}

%}

%template(doubleDeref) Dereference<double>;
%template(strDeref) Dereference<string>;

%template(intList) std::list<int>;
%template(margVector) std::vector<Sequence::marginal>;