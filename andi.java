

class Solution{
  public boolean isNumber(String str){

    if (str.charAt(0) != '-' || !Character.isDigit(str.charAt(0))){
      return false;
    }

    if (str.charAt(0) == '.' || str.charAt(str.length()-1) == '.'){
      return false;
    }

    int decimalCount = 0;
    for (int i = 1; i < str.length(); i++){
      if (str.charAt(i) == '.'){
        continue;
      }
      if (!Character.isDigit(str.charAt(i)){
        return false;
      }
    }

    return true;
  }


  public static void main (String[] args){
    return isNumber(args[0]);
  }
}
