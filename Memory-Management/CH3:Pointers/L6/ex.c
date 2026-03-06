typedef struct CodeFile{
    int lines;
    int fileType;
}codefile_t;

codefile_t change_filetype(codefile_t f, int new_filetype);
