import React, { useState } from 'react';
import axios from 'axios';


const API_URL = 'http://127.0.0.1:8000/api/v1/hds/';


const STATUS_OPTIONS = [
    { value: 'LIVRE', label: 'Livre (Aguardando Projeto)' },
    { value: 'EM_USO', label: 'Em Uso (Projeto Ativo)' },
    { value: 'ARQUIVADO', label: 'Arquivado (Dados Completos)' },
    { value: 'MANUTENCAO', label: 'Manutenção/Defeito' },
];

const HDForm = ({ onHDCreated }) => {
 
    const [formData, setFormData] = useState({
        nome_hd: '',
        serial_number: '',
        tamanho_total_gb: 0.00,
        localizacao: '',
        status: 'LIVRE', 
    });
    
    const [success, setSuccess] = useState(false);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            
            [name]: (name === 'tamanho_total_gb') ? parseFloat(value) : value,
        }));
    };

    // Manipulador de envio do formulário (POST)
    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setSuccess(false);

        try {
            await axios.post(API_URL, formData);
            
            // Sucesso: Limpa o formulário e notifica o componente pai
            setSuccess(true);
            setFormData({ // Reseta para valores iniciais
                nome_hd: '', serial_number: '', tamanho_total_gb: 0.00,
                localizacao: '', status: 'LIVRE',
            });
            
            // Notifica o HDList para recarregar a lista
            if (onHDCreated) {
                onHDCreated(); 
            }

        } catch (err) {
            console.error("Erro no cadastro:", err.response ? err.response.data : err.message);
            // Exibe erros de validação do Django para o usuário
            setError(err.response ? JSON.stringify(err.response.data) : "Erro ao cadastrar. Tente novamente.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="p-6 bg-white shadow rounded-lg">
            <h2 className="text-2xl font-semibold mb-4 text-indigo-700">Cadastrar Novo HD</h2>
            
            {success && <div className="p-3 mb-4 bg-green-100 text-green-700 rounded">HD cadastrado com sucesso!</div>}
            {error && <div className="p-3 mb-4 bg-red-100 text-red-700 rounded">Erro: {error}</div>}

            <form onSubmit={handleSubmit} className="space-y-4">
                {/* Nome do HD */}
                <div>
                    <label htmlFor="nome_hd" className="block text-sm font-medium text-gray-700">Nome do HD</label>
                    <input type="text" name="nome_hd" id="nome_hd" required
                        value={formData.nome_hd} onChange={handleChange}
                        className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
                    />
                </div>

                {/* Serial Number */}
                <div>
                    <label htmlFor="serial_number" className="block text-sm font-medium text-gray-700">Serial Number</label>
                    <input type="text" name="serial_number" id="serial_number" required
                        value={formData.serial_number} onChange={handleChange}
                        className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
                    />
                </div>

                {/* Tamanho Total (GB) */}
                <div>
                    <label htmlFor="tamanho_total_gb" className="block text-sm font-medium text-gray-700">Tamanho Total (GB)</label>
                    <input type="number" step="0.01" name="tamanho_total_gb" id="tamanho_total_gb" required
                        value={formData.tamanho_total_gb} onChange={handleChange}
                        className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
                    />
                </div>

                {/* Localização */}
                <div>
                    <label htmlFor="localizacao" className="block text-sm font-medium text-gray-700">Localização</label>
                    <input type="text" name="localizacao" id="localizacao" required
                        value={formData.localizacao} onChange={handleChange}
                        className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
                    />
                </div>

                {/* Status */}
                <div>
                    <label htmlFor="status" className="block text-sm font-medium text-gray-700">Status</label>
                    <select name="status" id="status" required
                        value={formData.status} onChange={handleChange}
                        className="mt-1 block w-full p-2 border border-gray-300 rounded-md shadow-sm"
                    >
                        {STATUS_OPTIONS.map(option => (
                            <option key={option.value} value={option.value}>
                                {option.label}
                            </option>
                        ))}
                    </select>
                </div>

                <button
                    type="submit"
                    disabled={loading}
                    className={`w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white ${loading ? 'bg-indigo-400 cursor-not-allowed' : 'bg-indigo-600 hover:bg-indigo-700'}`}
                >
                    {loading ? 'Cadastrando...' : 'Cadastrar HD'}
                </button>
            </form>
        </div>
    );
};

export default HDForm;