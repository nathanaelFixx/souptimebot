#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <strings.h>
#include <netinet/tcp.h>
#include <sys/uio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <stdio.h>
#include <string.h>



int main (int argc, char* argv[]) {
	const int server_port = 3579;
	char send_string[256];	
	char server_name[] = "127.0.0.1";

	printf("What should I send?\n");
	scanf("%s", send_string);
	

	// figure out the IP address
	struct hostent* host = gethostbyname(server_name);
	// set up the data structure
	sockaddr_in sendSockAddr;
	bzero((char*) &sendSockAddr, sizeof(sendSockAddr));
	sendSockAddr.sin_family = AF_INET;
	sendSockAddr.sin_addr.s_addr = inet_addr(inet_ntoa(*(struct in_addr*)*host->h_addr_list));
	sendSockAddr.sin_port = htons(server_port);

	// create the socket
	
	int clientSd = socket(AF_INET, SOCK_STREAM, 0);

	// connect <-- this makes me a client!
	
	int connectStatus = connect(clientSd, (sockaddr*)&sendSockAddr, sizeof(sendSockAddr));

	if(connectStatus < 0) {
		printf("Failed to connect");
		return -1;
	}

	int write_result = write(clientSd, send_string, strlen(send_string));

	char result_value[256];
	int nRead = read(clientSd, result_value, strlen(send_string));
	printf ("\n%s\n", send_string);
	close(clientSd);
	return 0;
}
