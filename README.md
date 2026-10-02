# Windows VM Cloud

Projeto inicial para um serviço de Windows virtual acessível pelo navegador.

- `frontend/`: painel que pode ir para GitHub Pages.
- `backend/`: API de sessões.
- A API deste pacote é um esqueleto: ela **não cria uma VM Windows real ainda**.

Para uma VM real, o servidor precisa de KVM/QEMU/libvirt ou Hyper-V, uma instalação/licença do Windows, recursos de CPU/RAM/disco e um console remoto como noVNC ou Apache Guacamole. Também são necessários autenticação, isolamento, limites de recursos e limpeza das VMs.

Não coloque uma ISO do Windows no GitHub. O GitHub Pages hospeda o painel; a VM deve rodar em um servidor separado.
