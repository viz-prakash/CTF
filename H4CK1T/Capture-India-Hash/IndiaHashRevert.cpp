#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>

#define delims " \t"

typedef std::pair<std::string, char> char_map_pair;

std::map<std::string, char> charmap;

void parseline(std::string line) {
	if (line == "") {
		return;
	}
	int start = 0;
	bool keyflag = false;
	int end;
	std::string key, value;
	while (true) {
		end = line.find_first_of(delims, start);
		if (end == std::string::npos) {
			if (keyflag) {
				value = line.substr(start, end);
			}
			break;
		}
		if (start != end) {
			if (!keyflag) {
				key = line.substr(start, end);
				keyflag = true;
			}
			else {
				value = line.substr(start, end);
				break;
			}
		}
		start = end + 1;
	}
	//hardcoded specific for problem
	//if (value.size() > 8) {
	//	value.erase(value.begin() + 4, value.end());
	//}
	std::pair < std::string, char> keyval(value.substr(0, 4), key.c_str()[0]);
	charmap.insert(keyval);
	std::pair< std::string, char> keyval2(value.substr(value.size() - 4), key.c_str()[0]);
	charmap.insert(keyval2);
	//return keyval;
}

void readfile_gen_charmap(std::string filename) {
	std::ifstream filestream;
	filestream.open(filename); //default ios::in is assumed
							   //filestream.open(filename, ios::in);
	std::string line;
	while (std::getline(filestream, line)) {
		//std::stringstream strstream(line);
		/*while (std::getline(strstream, token, '\t')) {
		}*/
		//charmap.insert(parseline(line));
		parseline(line);
	}

	std::cout << "done reading char map" << std::endl;
	filestream.close();
}


int main() {
	std::string exitstring;
	while (1) {

		std::string target_hash;
		std::cin >> target_hash;

		if (target_hash == "exit" || target_hash == "q")
			break;

		readfile_gen_charmap("charmap.txt");
		std::string unhashed_string;
		//std::vector<char> char_target_hash(target_hash.begin(), target_hash.end());
		//char_target_hash.push_back('\0');
		int start = 0;
		while (start < target_hash.size() - 8) {
			std::string key = target_hash.substr(start, 4);
			char mapped_char = charmap[key];
			if ((mapped_char < 48 || mapped_char > 57) && (mapped_char < 65 || mapped_char > 90) && (mapped_char < 97 || mapped_char > 122)) {
				std::cout << "mapping not found for " << key << std::endl;
			}
			else {
				unhashed_string.insert(unhashed_string.end(), mapped_char);
			}
			start += 4;
		}
		std::string key = target_hash.substr(start, 4);
		char mapped_char = charmap[key];
		if ((mapped_char < 48 || mapped_char > 57) && (mapped_char < 65 || mapped_char > 90) && (mapped_char < 97 || mapped_char > 122)) {
			std::cout << "mapping not found for " << key << std::endl;
			key = target_hash.substr(start, 8);
			mapped_char = charmap[key];
			if ((mapped_char < 48 || mapped_char > 57) && (mapped_char < 65 || mapped_char > 90) && (mapped_char < 97 || mapped_char > 122)) {
				std::cout << "mapping not found for " << key << std::endl;
			}
			else {
				unhashed_string.push_back(mapped_char);
			}
		}
		else {
			unhashed_string.insert(unhashed_string.end(), mapped_char);
			start += 4;
			key = target_hash.substr(start, 4);
			mapped_char = charmap[key];
			if ((mapped_char < 48 || mapped_char > 57) && (mapped_char < 65 || mapped_char > 90) && (mapped_char < 97 || mapped_char > 122)) {
				std::cout << "mapping not found for " << key << std::endl;
			}
			else {
				unhashed_string.insert(unhashed_string.end(), mapped_char);
			}
		}
		std::cout << "Done processing" << std::endl;

		std::cout << "unhashed String : " << unhashed_string << std::endl;
	}
	return 0;
}