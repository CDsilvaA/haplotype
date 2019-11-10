# mtx_sparse_hap.R: Creates a sparse matrix using information from the haplotype block output. 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# author = ["Cherlynn Daniela da Silva Arce <cdnsprado@gmail.com>", "Thiago Roberto do Prado <trprado@outlook.com>"
# license__ = "GPL3"
# version__ = "1.0"

path<-"/home/Dev/python-markers" # path
lista<-list.files(path) # lists the files in the python-markers folder
setwd(path) # directoy
library(Matrix)

mb<-list()
for(i in 1:length(lista)){ 
  dado<-file(lista[i]) # each element of the list will be a file 
  mylist<-strsplit(readLines(dado)," ") # imports the elements of the list
  close(dado)
  
  max<-0 
  for(j in 1:length(mylist)){ # checks which is the largest number of columns to create the matrix
    if(length(mylist[[j]]) > max)
      max<-length(mylist[[j]])
  }
  
  ma<-Matrix(0,nrow=length(mylist),ncol=max,sparse=TRUE) # zero sparse matrix
  for(k in 1:length(mylist)){
    vect<-as.integer(unlist(mylist[[k]],""))
    for(l in 1:length(vect)){
      ma[k,l]<-vect[l] # saves the respective list element in the matrix elements
    }
  }
  mb[[i]]<-ma # list with several matrices
}
  
maxcols<-0
for(a in 1:length(mb)){ # checks the maximum number of columns of all elements in the list
  if(ncol(mb[[a]]) > maxcols)
    maxcols <- ncol(mb[[a]])
}
sumrows<-0
for(u in 1:length(mb)){  # adds the lines of the list elements
  sumrows<-sumrows + nrow(mb[[u]])
}

mc<-mb[[1]]
for(t in 2:length(mb)){  # joins all matrices (append matrix)
  mc<-rbind(mc,mb[[t]])
}
mc # final result

